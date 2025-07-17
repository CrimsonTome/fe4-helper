from flask import Blueprint, render_template, current_app
import csv

views = Blueprint(__name__, "views")
@views.route("/")
def index():
    csv_path = current_app.root_path + "/static/data/first-gen-character-bases.csv"
    with open(csv_path) as file:
        reader = csv.reader(file)
        return render_template("first-gen-character-stats.html.jinja", csv=reader)
