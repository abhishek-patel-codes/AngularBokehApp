from flask_pymongo import PyMongo
from flask import Flask

app = Flask(__name__)
tenant = "Demo"
app.config["MONGO_URI"] = "mongodb://localhost:27017/" + tenant
mongo = PyMongo(app)

if __name__ == '__main__':
    mongo.db.mapped_user_details.drop()
    data_1 = {
        "FirstName": "Shibbu", 
        "LastName": "Sharma", 
        "Email": "ssemail@gmail.com11", 
        "gender": "male", 
        "plan": "platinum"
    }
    mongo.db.user_details.insert_one(data_1)

#    data_1 = {
#        "user": "john_2",
#        "alternate_user": "john_admin_2"
#    }
#    mongo.db.mapped_user_details.insert_one(data_1)
#
#    data_1 = {
#        "user": "john_2",
#        "alternate_user": "asd"
#    }
#    mongo.db.mapped_user_details.insert_one(data_1)
