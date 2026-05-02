from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///class&student.sqlite3"

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# models
class Student(db.Model):
    std_id = db.Column(db.Integer, primary_key = True)
    std_name = db.Column(db.String(40), nullable = False)
    std_class = db.relationship('Class', backref = "student")

class Class(db.Model):
    id  = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(40), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('student.std_id'), nullable = False)


if __name__ == "__main__":
    app.run(debug=True)