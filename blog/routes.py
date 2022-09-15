from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from blog import models
from config import Config
from flask import render_template, Flask

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
  return {
      "db": db,
      "Entry": models.Entry
  }


@app.route("/")
def homepage():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html")
