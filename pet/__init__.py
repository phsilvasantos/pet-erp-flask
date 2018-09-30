"""App configuration."""

from flask import Flask
from pet.core.views import core
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


# BLUEPRINT CONFIGS #######

app.register_blueprint(core)

# DB Config

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)
