#!/usr/bin/python3
import json
from pymongo import MongoClient
from bson.json_util import dumps

db_user = "admin"
db_pass = "admin"  
dbconnect = MongoClient('mongodb://%s:%s@x.x.x.x:27017' % (db_user, db_pass))
dbname = dbconnect["clients"]
collection = dbname["client"]


def insert_mongo_document():
    document = { 
    "clientID": "000001",
    "name": "SuperDuperClient",   
    "company":"SuperDuperClient",
    "address":"The corner of the moon, 22",
    "city":"The Moon, Space",
    "phone":"+000 000 00 00 01",
    "mail":"info@SuperDuperClient.com",
    "contract": "Traditional",
    "scope": "Automation & Cloud Specialist"
    }
    insert = collection.insert_one(document)
    #print(insert)


# I use  {'_id': False} to avoid show mongodb ID in my output
def find_mongo_document(key, value):   
    # Query find only one document, and remove mongo _id from output
    mongoquery = collection.find_one({ key : value }, {'_id': False}) 
    # Transform output to json and filter by "key"  
    json_mongoquery = json.dumps(mongoquery[key])  
    # Transform filtered "key" output to string and remove cuotes                     
    json_mongoquery_str = str(json_mongoquery).strip('"')     
    # Print in plain text my result of query          
    print(json_mongoquery_str)                                          


find_mongo_document("company", "SuperDuperClient")
