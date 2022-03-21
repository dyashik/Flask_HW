from app import myobj
from flask import render_template

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]


#view function
@myobj.route("/")
@myobj.route("/index.html")
def home():

    return render_template("home.html", name = name, city_names = city_names)

#myobj.run()