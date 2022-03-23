
from app import myobj

from flask import flash, get_flashed_messages, render_template, request

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

#view function
@myobj.route("/")
@myobj.route("/index.html")
def home():
    return render_template("home.html", name = name, city_names = city_names, list = "", val = False)

# @myobj.route("/random")
# def new_page():
#     return render_template("home.html", name = name, city_names = city_names, list = ["dad"])

@myobj.route("/newCity", methods = ["POST", "GET"])
def someMethod():
    if request.method == "POST":
        var = request.form['box']
        flash(var)
        return render_template("home.html", name = name, city_names = city_names, list = var, val = True)

