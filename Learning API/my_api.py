from flask import Flask,request
from flask_restful import Api, Resource

app = Flask(__name__)

data = [
        {"name":"Alex", "Password":"Alex99", "Age":21 },
        {"name":"Bob", "Password":"Bob99", "Age":19 },
        {"name":"Charlie", "Password":"Charlie99", "Age":22},
        {"name":"Mandy", "Password":"Mandy99", "Age":23 }
        ]

@app.route("/get_data") # by default method is GET
def index():
    return data, 200

@app.route("/get_user/<string:user>")
def get_user(user):
    for user_dict in data:
        if user_dict["name"] == user:
            return user_dict, 200
        
    # return {"message": "User not found"} # but status code will be 200 OK not 404
    # to change response status code to 404 do
    return {"message": "User not found"}, 404

@app.route("/add_user", methods = ["POST"])
def insert():
    new_user = request.get_json() # not json only use get_json
    user_name = new_user["name"]
    Pass = new_user["Password"]
    Age = new_user["Age"]
    # data.append({"name" :user_name, "Password": Pass, "Age":Age})
    data.append(new_user)
    # return "<p>User added successfully</p>"
    return {"message": "User added successfully"}, 201
    # 201 -- resource created

# print(data)

app.run(debug=True)