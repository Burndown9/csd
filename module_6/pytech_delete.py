""" 
    Title: pytech_delete.py
    Author: Jacob Hayes
    Date: 7 Feb 2021
    Description: Test program for deleting documents from the pytech collection,
                using Professor Krasso's code as a template
"""

""" import statements """
from pymongo import MongoClient #pymongo lets us interface with MongoDB

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.lazzm.mongodb.net/pytech"

# connect to the MongoDB cluster 
client = MongoClient(url) #turns our connection string into a client we can interface

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students #(aka MongoClient(url).pytech.students)

# find all students in the collection 
student_list = students.find({}) #without anything in {} returns all

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# test document 
test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

# insert the test document into MongoDB atlas 
test_doc_id = students.insert_one(test_doc).inserted_id
#this inserts test_doc using insert_one and then returns the inserted_id to 
#test_doc_id for us to display to the user

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# call the find_one() method by student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list: #a for loop goes through every item in the collection
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")