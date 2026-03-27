from flask import Flask
from flask import render_template
from flask import request
# from flask import Flask, render_template, request
from flask import redirect, url_for


app = Flask(__name__)

@app.route("/index", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        fname = request.form.get("user_fname")
        lname = request.form.get("user_lname")
        gender = request.form.get("gender")
        address = request.form.get("c_address")
        phone = request.form.get("phone")
        
        if gender=="male":
            return render_template("display.html", name = fname, c_address = address, phone = phone, gender = "Boys")
        elif gender=="female":
            return render_template("display.html", name = fname, c_address = address, phone = phone, gender = "Girls")

    # default method is GET then return this page (alternate hai you can use if request.method == "GET" )
    return render_template("register.html")

# print(url_for("index"))

# url_for takes function name (string) as argument and returns url for that function
# redirect as name suggest redirects to given url --> takes url as an argument in string format
@app.route("/home",methods = ["GET","POST"])
def redirect_(): # change function name
    return redirect(url_for("index"))

# When ever given error (404 here) will occur this definition will get executed
@app.errorhandler(404)
def page_not_found(e):
    return "Page Not Found 404 -- Page Not Defined or No route defined for this url/endpoint" \
    "\n OR your on wrong url try visiting index page"

if __name__ == "__main__":
    app.run(debug=True)