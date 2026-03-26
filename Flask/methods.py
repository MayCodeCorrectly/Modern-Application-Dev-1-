from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_func():
    return "GET"

@app.route("/", methods=["POST"])
def post_func():
    return "POST"

app.run(debug=True)