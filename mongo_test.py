import pymongo
import os
import ssl
import pprint

if os.path.exists("env.py"):
    import env

client = pymongo.MongoClient(os.environ.get("MONGO_URI"), ssl_cert_reqs=ssl.CERT_NONE)

db = client['product-app']

customers = db.customers

for customer in customers.find():
    pprint.pprint(customer)