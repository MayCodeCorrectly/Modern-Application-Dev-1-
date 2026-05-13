from flask import Flask
app = Flask(__name__)

@app.route('/user')
def index():
    return "Hello user!"

app.run(debug=True)
