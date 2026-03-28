# import flask first and necessary things
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for # to get the url 
from flask import redirect
# from flask_sqlalchemy import SQLAlchemy # for SQLite3

# make instance/object of Flask class
app = Flask(__name__,template_folder="views") # Since default folder is "templates" direct it to "views"
print(type(app))

@app.route("/") # root or base url --> http://127.0.0.1:5000  or http://localhost:5000
# This binds the url with definition written below it,
# It is a decorator function/method which binds teh function with url
def root():
    return "<h1>Hello World!!<h1>"

""" Now browser will execute this function when client visits this url which will cause the rendering of
template we are returning """

""" if two functions have same endpoints then first one that matches a url gets executed """

@app.route("/")
def index():
    return "<h1>This is latest definition for this url but it will not be displayed</h1>"

# """ If two routes have same function/definition name then flask throws assertion error """

@app.route("/login",methods = ["GET","POST"]) # these /login are called endpoints
@app.route("/sign-in",methods = ["GET","POST"]) # both urls binds to same definition
# visiting anyone will cause execution of same function/definition
def login():
    if request.method == "GET":
        return render_template("login_page.html")
    else:
        return render_template("Error_Page.html")

@app.route("/greetings",methods = ["POST"])
def greet():
    if request.method == "POST":
        user_name = request.form["user_fname"]
        user_gender = request.form["gender"]
        if user_gender=="male":
            return render_template("greetings.html",user_fname=user_name,user_gender="Boys")
        elif user_gender=="female":
            return render_template("greetings.html",user_fname=user_name,user_gender="Girls")
        else:
            return render_template("greetings.html",user_fname=user_name)

if __name__ == "__main__":
    app.run(debug=True) 