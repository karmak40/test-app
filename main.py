from typing import Union
from pymongo import MongoClient
import os
import certifi
from fastapi import FastAPI
 
app = FastAPI()

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   # os.environ (variable name, default value if variable is null)
   CONNECTION_STRING = os.environ.get("DATABASE_URL", "mongodb://localhost:27017/")

   ca = certifi.where()
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING, tlsCAFile=ca)

   # Create or connect the database for our example (we will use the same database throughout the tutorial
   return client["school"]

def get_students():

    dbname = get_database()
    # Retrieve a collection named "students" from database
    #collection_name = dbname["students"]
    res = "All collections: "
    for coll in dbname.list_collection_names():
         res += coll
    return res
   

@app.get("/")
def read_root():
    res = get_students()
    return {"message": "Guten Tag Frau Pyzh, Ich möchte dich küssen :) " + res}