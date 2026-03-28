from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) # make object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(current_dir,"testdb.sqlite3")  #to connect to database 
db = SQLAlchemy(app) # db object # to make connection of app with db object

app.app_context().push() # to combine the context of backend and app

# make a class in which each tuple in database is object
class User(db.Model):
    # __tablename__ = "user" 
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String(), nullable = False)
    user_gender = db.Column(db.String(), nullable = False)
    user_age = db.Column(db.Integer, nullable = False)

# getting an idea    
print(User.query.all()) # confirmation

tuples = User.query.all()
print(type(tuples[0]))
for object in tuples:
    print(object.user_id,object.user_name,object.user_gender,object.user_age)

    #  ======== CRUD operation =========== #

# add / create
db.create_all()
new_user = User(user_name= "Mainsh", user_gender ="M", user_age = 20)
db.session.add(new_user)
# db.session.commit() # Since manish is already (in first execution) added so need to commit it again

#The many times you execute this that many times "mainsh" will get added 

#read
user_1 = User.query.get(1)
print(user_1.user_name,type(user_1))

# read without primary  key or based on other attributes
user_list = User.query.filter_by(user_name="Khushi").all()
print(user_list) # it gives the list of all the user which match the filter condition

user_list = User.query.filter_by(user_name="Khushi").first()
print(user_list) # it give the of first user which matches the filter condition


#update
user_1.user_age = 212
db.session.commit() # to reflect changes in database

#delete 
user = User.query.filter_by(user_name = "Ritesh").first()
print(user)
db.session.delete(user)
db.session.commit()
