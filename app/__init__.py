from flask import Flask, request, url_for
from flask_jsglue import JSGlue
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from app import helpers
from tempfile import mkdtemp

# initialize Flask instance
app = Flask(__name__)
db = SQLAlchemy(app)

from app import views, models

# use JSGlue to allow JS to call url_for
JSGlue(app)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure Flask session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

