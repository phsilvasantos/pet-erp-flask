"""App configuration."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'mysecret'


# BLUEPRINT CONFIGS #######

# DB Config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


from petshop.core.views import core
app.register_blueprint(core)
