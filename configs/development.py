import os

SECRET_KEY = b'F\x9c\x83.\xca\x0e\xa3\xa9\x8b=\xeaDo\xc1\x99\xddp]@\xaa\xcfOG\x0f'
DEBUG = True
# DATABASE = "/vagrant/blog.db"
SQLALCHEMY_DATABASE_URI = "sqlite:////vagrant/blog.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL="pyamqp://guest@localhost//"
EMAIL_USERNAME = os.environ.get("MDBLOG_EMAIL_USERNAME", None)
EMAIL_PASSWORD = os.environ.get("MDBLOG_EMAIL_PASSWORD", None)