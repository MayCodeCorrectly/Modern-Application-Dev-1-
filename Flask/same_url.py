from flask import Flask

app = Flask(__name__)

@app.route("/")
def first():
    return "First"

@app.route("/")
def second():
    return "Second"

app.run(debug=True)


"""
Flask registers rules in order:

Rule 1 → / → first
Rule 2 → / → second

Flask does NOT overwrite, it keeps both.

Key point (important)

Flask’s routing uses first match wins, not last
"""