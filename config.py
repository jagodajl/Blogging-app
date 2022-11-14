import os

class Config(object):
    DEBUG = os.environ.get("BUG_SET")
    DEVELOPMENT = os.environ.get("DEV_SET")
    FLASK_HTPASSWD_PATH = "/secret/.htpasswd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = "sqlite:///data_blog.db"
    # ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "")
    ADMIN_USERNAME = "admin"
    # ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")
    ADMIN_PASSWORD = "admin"
