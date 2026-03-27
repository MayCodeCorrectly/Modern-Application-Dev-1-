from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/register",methods = ["GET","POST"])
def registration_page():
    if request.method == "POST":
        name = request.form.get("name")
        gender = request.form.get("gender")
        age = request.form.get("age")
        qual = request.form.get("qual")
        stream = request.form.get("stream")
        address = request.form.get("address")
        image = request.form["image"]
        
        return render_template("review.html", name=name , gender=gender, age=age, qual=qual, stream=stream, address=address, image=image)
        
    return render_template("registration_form.html")

@app.route("/success")
def success():
    return "<h3>Your registration is successful!!"

if __name__=="__main__":
    app.run(debug=True)