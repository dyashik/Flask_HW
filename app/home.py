from flask import Flask, render_template
from flask import escape

myobj = Flask(__name__)
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]


#view function
@myobj.route("/")
@myobj.route("/index.html")
def home():

    return render_template("home.html", name = name, city_names = city_names)

#myobj.run()