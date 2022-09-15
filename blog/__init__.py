from routes import app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from blog import routes, models

# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# @app.shell_context_processor
# def make_shell_context():
#   return {
#       "db": db,
#       "Entry": models.Entry
#   }

if __name__ == '__main__':
    app.run(debug=True)
