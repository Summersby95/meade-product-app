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
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def get_upcoming():
    if not(session.get("user")):
        flash("Please login to view this content")
        return redirect(url_for("login"))

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


@app.route("/view_product/<product_id>")
def view_product(product_id):
    if not(session.get("user")):
        flash("Please login to view this content")
        return redirect(url_for("login"))
    
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    return render_template("view_product.html", product=product)


@app.route("/create_product/customer_select", methods=["GET", "POST"])
def customer_select():
    if not(session.get("user")):
        flash("Please login to view this content")
        return redirect(url_for("login"))
    elif session["role"] != "Commercial":
        flash("You do not have permission to create products")
        return redirect(url_for("get_upcoming"))

    if request.method == "POST":
        return redirect(
            url_for("product_details", customer_id=request.form.get("customer"))
        )

    customers = mongo.db.customers.find().sort('customer_name', pymongo.ASCENDING)
    return render_template("customer_select.html", customers=customers)


@app.route("/create_product/product_details/<customer_id>", methods=["GET", "POST"])
def product_details(customer_id):
    if not(session.get("user")):
        flash("Please login to view this content")
        return redirect(url_for("login"))
    elif session["role"] != "Commercial":
        flash("You do not have permission to create products")
        return redirect(url_for("get_upcoming"))

    customer_name = mongo.db.customers.find_one({"_id": ObjectId(customer_id)})["customer_name"]

    field_list = mongo.db.form_fields.find_one({
        "customer": customer_name, 
        "department": session["department"]
    })

    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})

    for field in field_list["commercial_details"]:
        if (field["field_type"] == "multiselect") or (field["field_type"] == "select"):
            if field["options_type"] == "table":
                field["options"] = mongo.db[field["table_name"]].find()

    return render_template("commercial_product_details.html", customer_name=customer_name, field_list=field_list)
    


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user"):
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
    if session.get("user"):
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