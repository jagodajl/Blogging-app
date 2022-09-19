from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

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


from blog import models
from blog import routes

if __name__ == '__main__':
    app.run(debug=True)
