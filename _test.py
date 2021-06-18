import os
import pymongo
import pytest
if os.path.exists("env.py"):
    import env


def test_vars_exist():
    envs = [
        "IP",
        "PORT",
        "SECRET_KEY",
        "MONGO_URI",
        "MONGO_DBNAME",
        "EMAIL_LOGIN",
        "EMAIL_PASS"]
    if os.path.exists("env.py"):
        for x in envs:
            assert os.getenv(x) is not None, \
                "Please set environment variable '{}'".format(x)
    else:
        assert os.path.exists("env.py"), "Create an env.py file"


client = pymongo.MongoClient(
    os.environ.get("MONGO_URI"),
    serverSelectionTimeoutMS=5000)


def test_mongo():
    try:
        client.server_info()
    except BaseException:
        raise ConnectionError("Invalid Mongo URI Connection String")


def test_db():
    try:
        assert os.environ.get("MONGO_DBNAME") in client.list_database_names(
        ), "Database '{}' does not exist".format(
                os.environ.get("MONGO_DBNAME"))
    except BaseException:
        raise ConnectionError("Connection could not be made")


if os.path.exists("env.py"):
    db = client[os.environ.get("MONGO_DBNAME")]
else:
    db = client["None"]


def test_collections():
    colls = ["customers", "defects", "departments", "form_fields", "origins",
             "pack_info", "products", "roles"]
    for coll in colls:
        try:
            assert coll in db.list_collection_names(
            ), "Collection '{}' does not exist in database".format(coll)
        except BaseException:
            raise ConnectionError("Connection could not be made")


def test_product():
    product = db.products.find_one()
    keys = [
        "product_name",
        "department",
        "customer",
        "status",
        "start_date",
        "created_by"]
    if product is not None:
        for key in keys:
            assert key in product.keys(), \
                "Product object is missing '{}' key".format(key)
    else:
        raise FileNotFoundError("No product objects in collection")


def test_form_fields():
    field_list = db.form_fields.find_one()
    keys = [
        "customer",
        "department",
        "commercial_details",
        "packaging_details",
        "operations_details",
        "technical_details",
        "prophet_details"]
    if field_list is not None:
        for key in keys:
            for key in keys:
                assert key in field_list.keys(), \
                    "Form field object is missing '{}' key".format(key)
    else:
        raise FileNotFoundError("No Form Field objects in collection")
