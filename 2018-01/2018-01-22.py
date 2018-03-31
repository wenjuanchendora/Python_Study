"""
远程操作mongodb
http://api.mongodb.com/python/current/installation.html
http://api.mongodb.com/python/current/tutorial.html

pip install pymongo
"""
from pymongo import MongoClient

client= MongoClient('mongodb://118.31.19.120:27017/')

# print(client.database_names())

db = client.get_database('node_club_dev')

collections = db.collection_names()
# print(collections)

users = db.get_collection('users')

# users.find_one_and_update({"loginname" : "username"},{'$set':{"active" : True}})
users.update_one({"loginname" : "username"},{'$set':{"active" : False}})
user = users.find_one({"loginname" : "username"})
print(user)