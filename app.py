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
    products = list(mongo.db.products.find().sort([
        ('start_date', pymongo.ASCENDING)
    ]))

    for product in products:
        product["start_date"] = product["start_date"].strftime("%d %B %Y")

    return render_template("upcoming_products.html", products=products)


@app.route("/view_product/<product_id>")
def view_product(product_id):
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    return render_template("view_product.html", product=product)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)