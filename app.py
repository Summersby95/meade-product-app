import os
from datetime import datetime, timedelta
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash
import email_func
import security
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Default Route
@app.route("/")
def get_upcoming():
    # The check login function (in the security.py file) checks that the user is logged in
    # All views are locked to the user unless they are logged in, they will be directed to the login screen
    if security.check_login():
        # get product list from products table, we only want certain columns, the rest will be
        # viewable in the view_product route, we also order by start_date to show urgent ones first
        products = list(mongo.db.products.find({}, {
            "product_name": 1,
            "department": 1,
            "customer": 1,
            "status": 1,
            "start_date": 1,
            "created_by": 1,
            "created_on": 1
        }).sort([
            ('start_date', pymongo.ASCENDING)
        ]))

        # we convert the start_date, which is a datetime object in the database, to a string
        for product in products:
            product["start_date"] = product["start_date"].strftime("%d %B %Y")

        return render_template("upcoming_products.html", products=products)
    else:
        # if the user is not logged in we redirect them to the login screen
        flash("Please login to view this content")
        return redirect(url_for("login"))


# View Product Details Route
@app.route("/view_product/<product_id>")
def view_product(product_id):
    if security.check_login():
        # Get the product document from the database using the product_id
        product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
        # Get a list of the roles from the roles table, we will use this to cycle
        # Through to show different roles details for the product
        # we dont include the admin/commercial/management roles as they dont have
        # specific role details for a product
        roles = list(mongo.db.roles.find({
            "role_name": {"$nin": ["Admin", "Commercial", "Management"]}
        }))
        return render_template("view_product.html", product=product, roles=roles)
    else:
        flash("Please login to view this content")
        return redirect(url_for("login"))


# Create Product Customer Select Route
@app.route("/create_product/customer_select", methods=["GET", "POST"])
def customer_select():
    if not(security.check_login()):
        flash("Please login to view this content")
        return redirect(url_for("login"))
    elif session["role"] != "Commercial":
        # Only a member of the commercial team has permission to create products
        flash("You do not have permission to create products")
        return redirect(url_for("get_upcoming"))
    else:
        # This view simply allows the user to select the customer the product is for
        # We do this first because the details required for a new product depend 
        # on the customer of the product. Therefore, to build the form with the 
        # correct fields we must first get the user to select the customer
        # the department is defined by the users attributes
        if request.method == "POST":
            return redirect(
                url_for("product_details", customer_id=request.form.get("customer"))
            )

        customers = mongo.db.customers.find().sort('customer_name', pymongo.ASCENDING)
        return render_template("customer_select.html", customers=customers)


# Create Product Product Details Route
@app.route("/create_product/product_details/<customer_id>", methods=["GET", "POST"])
def product_details(customer_id):
    if not(security.check_login()):
        flash("Please login to view this content")
        return redirect(url_for("login"))
    elif session["role"] != "Commercial":
        flash("You do not have permission to create products")
        return redirect(url_for("get_upcoming"))
    else:
        # get customer name using customer_id passed to url
        customer_name = mongo.db.customers.find_one({"_id": ObjectId(customer_id)})["customer_name"]

        # get field_list from form_fields table, searching on the customer name and department
        field_list = mongo.db.form_fields.find_one({
            "customer": customer_name, 
            "department": session["department"]
        })

        if request.method == "POST":
            user = mongo.db.users.find_one({"username": session["user"]})

            # Create product base details, common for all new products
            product = {
                "product_name": request.form.get("product_name"),
                "department": session["department"],
                "customer": customer_name,
                "status": "Pending - Awaiting Many",
                "start_date": datetime.strptime(request.form.get("start_date"), '%d %B, %Y'),
                "created_by": user["f_name"] + " " + user["l_name"],
                "created_on": datetime.now()
            }
            
            # From field_list, cycle through fields (which were used to build form) and get
            # value from post form with that field name and add detail to product dict
            # if it's a multiselect then create an list object and append every 
            # selected value to end of list
            for field in field_list["commercial_details"]:
                if field["field_type"] == "input":
                    product[field["field_name"]] = request.form.get(field["field_name"])
                elif field["field_type"] == "multiselect":
                    product[field["field_name"]] = []
                    for value in request.form.getlist(field["field_name"]):
                        product[field["field_name"]].append(value)

            # insert product dict into products table
            mongo.db.products.insert_one(product)

            # create email group to notify of new product creation
            # we only want to notify users of the same department or of the "All" department
            # we also only want the email attribute of the users
            email_group = mongo.db.users.find({
                "department": { "$in": [session["department"], "All"] },
                "username": { "$ne": session["user"] }
            }, {
                "email": 1
            })

            # convert dict into array of email addresses
            email_group_array = []

            for email in email_group:
                email_group_array.append(email["email"])

            # create message to send to users
            message = """
            A new product has been created for your department. 

            Product Name: %s
            User: %s
            
            Please login to the Meade Product App to view it: https://meade-product-app.herokuapp.com/
            """ % (request.form.get("product_name"), user["f_name"] + " " + user["l_name"])

            # call send_email function (view email_func.py) with email list, subject and message
            email_func.send_email(email_group_array, "A New Product Has Been Created", message)

            flash("Product Successfully Added")
            return redirect(url_for('get_upcoming'))
    

    # search the commercial_details objects in the field_list, if the field is a select 
    # or multiselect and has the "options_type" of "table" it means that it is using a table for 
    # options so we call the options from the table and create a list to store the options in and 
    # append it to the field object
    for field in field_list["commercial_details"]:
        if (field["field_type"] == "multiselect") or (field["field_type"] == "select"):
            if field["options_type"] == "table":
                options_table = mongo.db[field["table_name"]].find()
                field["options"] = []
                for option in options_table:
                    field["options"].append(option["name"])

    return render_template("commercial_product_details.html", customer_id=customer_id, field_list=field_list)


# My Tasks Route
@app.route("/my_tasks")
def my_tasks():
    if security.check_login():
        # if the user doesn't have a specific department then we don't need to filter on the department
        if session["department"] == "All":
            prod_fil = {}
        else:
            prod_fil = {"department": session["department"]}

        # if the user is part of the commercial team, we only want to see products which have the 
        # status of "Pending - Awaiting Commercial Sign Off"
        if session["role"] == "Commercial":
            role_fil = {"status": "Pending - Awaiting Commercial Sign Off"}
        else:
            role_fil = {}

        # We add the filter dictionaries we've created above as well as a filter to check 
        # if the product has an attribute equal to the users role (Commercial, Packaging, Operations...)
        # if the product has that attribute then the details for the users role have already
        # been completed and is not outstanding
        products = list(mongo.db.products.find({"$and": [prod_fil, role_fil, 
        {(session["role"].lower()): {"$exists": False}}]}, {
            "product_name": 1,
            "department": 1,
            "customer": 1,
            "status": 1,
            "start_date": 1,
            "created_by": 1
        }).sort([
            ('start_date', pymongo.ASCENDING)
        ]))

        return render_template("my_tasks.html", products=products)
    else:
        flash("Please login to view this content")
        return redirect(url_for("login"))


# Add Product Details Route
@app.route("/add_product_details/<product_id>", methods=["GET", "POST"])
def add_product_details(product_id):
    if security.check_login():
        # the form for adding product details will differ depending on the product and the role 
        # of the user
        role = session["role"]
        
        product = mongo.db.products.find_one({"_id": ObjectId(product_id)})

        # we get the customer and department from the product object
        customer = product["customer"]
        department = product["department"]

        # we get the field_list by searching with the customer and department
        # we only want the fields that are relevant for this user's role
        field_list = mongo.db.form_fields.find_one({
            "$and": [{"customer": customer}, {"department": department}]
        }, {(role.lower() + "_details"): 1})

        # we get a list of roles to cycle through when we are building the details tabs
        roles = list(mongo.db.roles.find({
            "role_name": {"$nin": ["Admin", "Commercial", "Management"]}
        }))

        

        if request.method == "POST":
            # we need the user's first and last name to put in the "added_by" field
            user = mongo.db.users.find_one({"username": session["user"]})

            # we start with an empty details dictionary
            details = {}

            # we cycle through the field_list and put all the details into the details dictionary
            for field in field_list[role.lower()+"_details"]:
                if field["field_type"] == "input" or field["field_type"] == "select":
                    details[field["field_name"]] = request.form.get(field["field_name"])
                elif field["field_type"] == "multiselect":
                    details[field["field_name"]] = []
                    for value in request.form.getlist(field["field_name"]):
                        details[field["field_name"]].append(value)
            
            # we then add the "added_by" and "date_added" fields to the dictionary so we know
            # when it was last updated
            details["added_by"] = user["f_name"] + " " + user["l_name"]
            details["date_added"] = datetime.now()
            
            # we then update the product and create an object of the role name which is equal to the 
            # dictionary we just created
            mongo.db.products.update_one({"_id": ObjectId(product_id)}, {
                "$set": {role.lower(): details}
            })

            # after updating we get the product object from the database again so that we can check 
            # what roles have submitted their information and which have not
            product = mongo.db.products.find_one({"_id": ObjectId(product_id)})

            outstanding_roles = []

            # we cycle through the roles and check if an object of the role exists within the product
            for role in roles:
                if not (role["role_name"].lower() in product):
                    outstanding_roles.append(role["role_name"])
            
            # if there are no outstanding roles left to input information then the product is ready 
            # to be signed off by commercial, if not then we give it the status of
            # "Pending - Awaiting " followed by the roles that have yet to submit information
            if len(outstanding_roles) == 0:
                status = "Pending - Awaiting Commercial Sign Off"
            else:
                status = "Pending - Awaiting " + (", ").join(outstanding_roles)
            
            mongo.db.products.update_one({"_id": ObjectId(product_id)}, {
                "$set": {"status": status}
            })

            email_group = mongo.db.users.find({
                "department": { "$in": [session["department"], "All"] },
                "username": { "$ne": session["user"] }
            }, {
                "email": 1
            })

            email_group_array = []

            for email in email_group:
                email_group_array.append(email["email"])

            message = """
            A product has been updated.

            Product Name: %s
            Customer: %s
            Department: %s
            User: %s
            
            You can view the product here: %s
            """ % (product["product_name"], product["customer"], product["department"], 
            user["f_name"] + " " + user["l_name"], "https://meade-product-app.herokuapp.com" + url_for("view_product", product_id=product_id))

            email_func.send_email(email_group_array, "A Product Has Been Updated", message)

            flash("Product Details Added Successfully")
            return redirect(url_for("my_tasks"))

        for field in field_list[role.lower() + "_details"]:
            if (field["field_type"] == "multiselect") or (field["field_type"] == "select"):
                if field["options_type"] == "table":
                    options_table = mongo.db[field["table_name"]].find()
                    field["options"] = []
                    for option in options_table:
                        field["options"].append(option["name"])

        return render_template("add_product_details.html", product=product, field_list=field_list, roles=roles)
    else:
        flash("Please login to view this content")
        return redirect(url_for("login"))


# Register Route
@app.route("/register", methods=["GET", "POST"])
def register():
    if security.check_login():
        # if the user is already logged in we don't want them registering again
        flash("You are already logged in")
        return redirect(url_for("get_upcoming"))

    if request.method == "POST":
        # we check to see if the username exists in the database already
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if user_exists:
            flash("This Username is taken!")
            return redirect(url_for("register"))
        # we check to see if the password and password_repeat values match
        elif request.form.get("password") != request.form.get("password_repeat"):
            flash("Passwords do not match!")
            return redirect(url_for('register'))
        # there is an environment variable with a hashed password
        # the user must input this password to gain be allowed to register
        # this is a security measure to prevent random people from being 
        # able to create accounts
        elif not(check_password_hash(os.environ.get("MEADE_PASS"), request.form.get("meade_password"))):
            flash("Incorrect Meade Passcode!")
            return redirect(url_for('register'))
        else:
            # if the form passes all checks then we create the user dictionary and insert it into the database
            user = {
                "username": request.form.get("username"),
                "f_name": request.form.get("f_name"),
                "l_name": request.form.get("l_name"),
                "email": request.form.get("email"),
                "password": generate_password_hash(request.form.get("password")),
                "department": request.form.get("department"),
                "role": request.form.get("role")
            }
            mongo.db.users.insert_one(user)

            session["user"] = request.form.get("username")
            session["department"] = request.form.get("department")
            session["role"] = request.form.get("role")
            flash("Registration Successful")
            return redirect(url_for("get_upcoming"))


    departments = list(mongo.db.departments.find().sort([
        ('department_name', pymongo.ASCENDING)
    ]))

    roles = list(mongo.db.roles.find().sort('role_name', pymongo.ASCENDING))

    return render_template("register.html", departments=departments, roles=roles)


@app.route("/login", methods=["GET", "POST"])
def login():
    if security.check_login():
        # if a user is already logged in we don't want them attempting to log in again
        flash("You are already logged in")
        return redirect(url_for("get_upcoming"))

    if request.method == "POST":
        # we check that the user exists exists and if the password provided matches the 
        # hash of the password in the database
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username")}
        )

        if user_exists:
            if check_password_hash(user_exists["password"], request.form.get("password")):
                # if it does then we set session variables for the user specifying their
                # username, department and role
                session["user"] = request.form.get("username")
                session["department"] = user_exists["department"]
                session["role"] = user_exists["role"]
                flash("You are logged in as {}".format(request.form.get("username")))
                return redirect(url_for("get_upcoming"))
            else:
                flash("Incorrect Username/Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username/Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# Log Out Route
@app.route("/logout")
def logout():
    # we remove the session variables when the user logs out
    flash("You have been logged out")
    session.pop("user")
    session.pop("department")
    session.pop("role")
    return redirect(url_for("login"))

# we start the app using the ip and port specified in the environment variables
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)