from flask import render_template

from blog import app


@app.route("/")
def homepage():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html")
