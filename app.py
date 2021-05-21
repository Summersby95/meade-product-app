import os
from datetime import datetime
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


@app.route("/")
def get_upcoming():
    if security.check_login():
        products = list(mongo.db.products.find({}, {
            "product_name": 1,
            "department": 1,
            "customer": 1,
            "status": 1,
            "start_date": 1,
            "created_by": 1
        }).sort([
            ('start_date', pymongo.ASCENDING)
        ]))

        for product in products:
            product["start_date"] = product["start_date"].strftime("%d %B %Y")

        return render_template("upcoming_products.html", products=products)
    else:
        flash("Please login to view this content")
        return redirect(url_for("login"))


@app.route("/view_product/<product_id>")
def view_product(product_id):
    if security.check_login():
        product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
        roles = list(mongo.db.roles.find({
            "role_name": {"$nin": ["Admin", "Commercial", "Management"]}
        }))
        return render_template("view_product.html", product=product, roles=roles)
    else:
        flash("Please login to view this content")
        return redirect(url_for("login"))


@app.route("/create_product/customer_select", methods=["GET", "POST"])
def customer_select():
    if not(security.check_login()):
        flash("Please login to view this content")
        return redirect(url_for("login"))
    elif session["role"] != "Commercial":
        flash("You do not have permission to create products")
        return redirect(url_for("get_upcoming"))
    else:
        if request.method == "POST":
            return redirect(
                url_for("product_details", customer_id=request.form.get("customer"))
            )

        customers = mongo.db.customers.find().sort('customer_name', pymongo.ASCENDING)
        return render_template("customer_select.html", customers=customers)


@app.route("/create_product/product_details/<customer_id>", methods=["GET", "POST"])
def product_details(customer_id):
    if not(security.check_login()):
        flash("Please login to view this content")
        return redirect(url_for("login"))
    elif session["role"] != "Commercial":
        flash("You do not have permission to create products")
        return redirect(url_for("get_upcoming"))
    else:
        customer_name = mongo.db.customers.find_one({"_id": ObjectId(customer_id)})["customer_name"]

        field_list = mongo.db.form_fields.find_one({
            "customer": customer_name, 
            "department": session["department"]
        })

        if request.method == "POST":
            user = mongo.db.users.find_one({"username": session["user"]})

            product = {
                "product_name": request.form.get("product_name"),
                "department": session["department"],
                "customer": customer_name,
                "status": "Pending - Awaiting Many",
                "start_date": datetime.strptime(request.form.get("start_date"), '%d %B, %Y'),
                "created_by": user["f_name"] + " " + user["l_name"],
                "created_on": datetime.now()
            }
            
            for field in field_list["commercial_details"]:
                if field["field_type"] == "input":
                    product[field["field_name"]] = request.form.get(field["field_name"])
                elif field["field_type"] == "multiselect":
                    product[field["field_name"]] = []
                    for value in request.form.getlist(field["field_name"]):
                        product[field["field_name"]].append(value)

            mongo.db.products.insert_one(product)

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
            A new product has been created for your department. 

            Product Name: %s
            User: %s
            
            Please login to the Meade Product App to view it: https://meade-product-app.herokuapp.com/
            """ % (request.form.get("product_name"), user["f_name"] + " " + user["l_name"])

            email_func.send_email(email_group_array, "A New Product Has Been Created", message)

            flash("Product Successfully Added")
            return redirect(url_for('get_upcoming'))
    

    for field in field_list["commercial_details"]:
        if (field["field_type"] == "multiselect") or (field["field_type"] == "select"):
            if field["options_type"] == "table":
                options_table = mongo.db[field["table_name"]].find()
                field["options"] = []
                for option in options_table:
                    field["options"].append(option["name"])

    return render_template("commercial_product_details.html", customer_id=customer_id, field_list=field_list)
    

@app.route("/my_tasks")
def my_tasks():
    if security.check_login():
        if session["department"] == "All":
            prod_fil = {}
        else:
            prod_fil = {"department": session["department"]}

        if session["role"] == "Commercial":
            role_fil = {"status": "Pending - Awaiting Commercial Sign Off"}
        else:
            role_fil = {}

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


@app.route("/add_product_details/<product_id>", methods=["GET", "POST"])
def add_product_details(product_id):
    if security.check_login():
        role = session["role"]
        
        product = mongo.db.products.find_one({"_id": ObjectId(product_id)})

        customer = product["customer"]
        department = product["department"]

        field_list = mongo.db.form_fields.find_one({
            "$and": [{"customer": customer}, {"department": department}]
        }, {(role.lower() + "_details"): 1})

        roles = list(mongo.db.roles.find({
            "role_name": {"$nin": ["Admin", "Commercial", "Management"]}
        }))

        details = {}

        if request.method == "POST":
            for field in field_list[role.lower()+"_details"]:
                if field["field_type"] == "input" or field["field_type"] == "select":
                    details[field["field_name"]] = request.form.get(field["field_name"])
                elif field["field_type"] == "multiselect":
                    details[field["field_name"]] = []
                    for value in request.form.getlist(field["field_name"]):
                        details[field["field_name"]].append(value)
            
            mongo.db.products.update_one({"_id": ObjectId(product_id)}, {
                "$set": {role.lower(): details}
            })

            outstanding_roles = []

            for role in roles:
                if not (role["role_name"].lower() in product):
                    outstanding_roles.append(role["role_name"])
            
            if len(outstanding_roles) == 0:
                status = "Pending - Awaiting Commercial Sign Off"
            else:
                status = "Pending - Awaiting " + (", ").join(outstanding_roles)
            
            mongo.db.products.update_one({"_id": ObjectId(product_id)}, {
                "$set": {"status": status}
            })

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


@app.route("/register", methods=["GET", "POST"])
def register():
    if security.check_login():
        flash("You are already logged in")
        return redirect(url_for("get_upcoming"))

    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if user_exists:
            flash("This Username is taken!")
            return redirect(url_for("register"))
        elif request.form.get("password") != request.form.get("password_repeat"):
            flash("Passwords do not match!")
            return redirect(url_for('register'))
        elif not(check_password_hash(os.environ.get("MEADE_PASS"), request.form.get("meade_password"))):
            flash("Incorrect Meade Passcode!")
            return redirect(url_for('register'))
        else:
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
        flash("You are already logged in")
        return redirect(url_for("get_upcoming"))

    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username")}
        )

        if user_exists:
            if check_password_hash(user_exists["password"], request.form.get("password")):
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


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    session.pop("department")
    session.pop("role")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)