""" 
    Title: mongodb_test.py
    Author: Jacob Hayes
    Date: 31 Jan 2021
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster, using Professor Krasso's
                 code as a template
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.lazzm.mongodb.net/pytech"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# show the connected collections 
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press Enter to exit... ")
