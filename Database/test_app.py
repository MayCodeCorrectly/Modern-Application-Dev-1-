from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test_db.db"
# This database will create only when you visit url ( in instance folder)

db = SQLAlchemy(app)

#  this will create db even if we don't visit URL
# with app.app_context():
#     db.create_all()


# create model --> ORM
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50), nullable = False)


@app.route("/")
def index():
    # db.drop_all()
    db.create_all() # create database
    # This will create the db only if we visit the url
    db.session.add_all([
        User(username = "Sandeep"),
        User(username = "Alex"),
        User(username = "Bob"),
        User(username = "Charlie")]
    )
    db.session.commit()
    return "Hello there!!"

if __name__ == "__main__":
    app.run(debug=True)