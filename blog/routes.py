from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html")
