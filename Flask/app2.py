from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        
        return render_template("display.html")
    
    # default method is GET then return this page (alternate hai)
    return render_template("register.html")
    

