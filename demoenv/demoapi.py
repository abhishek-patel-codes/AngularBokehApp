import flask
import json
from flask import request,jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo,MongoClient
from bson.json_util import dumps, loads 



app = flask.Flask(__name__)
app.config["DEBUG"]=True
CORS(app)

client=MongoClient()
mydb=client.Demo

    

@app.route('/view',methods=['GET'])

def data_all():
    
    datapy=mydb.user_details.find()
    datalist=list(datapy)
    data=dumps(datalist)
    return data

@app.route('/edit',methods=['GET'])
def get_data():
    email = request.args.get('email')

    datacur=mydb.user_details.find()
    datalist=list(datacur)
    data=dumps(datalist)
    datapy=json.loads(data)
    for d in datapy:
        if d['Email']==email:
            res=d
            break    
    return jsonify(res)  

@app.route('/add',methods=['POST'])
def add_data():

    datacur=mydb.user_details.find()
    datalist=list(datacur)
    data=dumps(datalist)
    datapy=json.loads(data)
    
    json_data = request.get_json()


    firstName = json_data['firstName']
    lastName = json_data['lastName']
    email = json_data['email']
    gender = json_data['gender']
    plan = json_data['plan']
    for i in datapy:
        if(i['Email']==email):
            message="failure"
        else:
            message="success"
    if(message=="success"):
        res={
            "FirstName":firstName,
            "LastName":lastName,
            "Email":email,
            "gender":gender,
            "plan":plan
            } 
        mydb.user_details.insert(res)    
        
    return jsonify({"status":message})            
                   
            
       
 

@app.route('/delete',methods=['DELETE'])
def del_data():
    email = request.args.get('email')
    
    mydb.user_details.delete_one({"Email": email})
           
    return jsonify({"status":"success"})  
          
  
    
if __name__ == "__main__":
    app.run(debug=True)
