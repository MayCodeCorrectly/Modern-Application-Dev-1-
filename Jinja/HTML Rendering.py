from jinja2 import Template

from flask import Flask
app = Flask(__name__)

stanza = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> 
    <title>Basic Tags</title>
</head>
<body style="background-color: bisque">
<hr>

{% for name in name_data -%}
<p style="font-size: large; background-color: aqua;">
    Hello {{name}}!! How is my web site looking?<br/>
</p>
{%- endfor %}
"""

names = ["Sandeep","Aniket","Pratham","Rohit"]

@app.route("/website") # url : localhost + website
def main():
    template = Template(stanza)
    return template.render(name_data= names)

# Call it to get file
def write_file():
    content = main()
    new_file = open("new_temp.html",mode="w")
    new_file.write(content)
    new_file.close()

# write_file()
# print(template.render(name_data=names)) This will get written in this # write_file()

# app.run(debug=True)


@app.route("/")
def temp1_render():
    # with open("blue_prints/temp1.html","r") as f:
    with open("MAD-1/Jinja/blue_prints/temp1.html", "r") as f: # this is relative to terminal location
        content = f.read()
        template = Template(content)
        print(template.render(name= "Sandeep"))

temp1_render()

# Better fix
from pathlib import Path

base = Path(__file__).parent
file_path = base / "blue_prints" / "temp1.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()