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


from petshop.views.views_cadastros import views_cadastros
from petshop.views.views_consultas import views_consultas
from petshop.views.views_vendas import views_vendas
from petshop.views.views_pagamentos import views_pagamentos

app.register_blueprint(views_cadastros)
app.register_blueprint(views_consultas)
app.register_blueprint(views_vendas)
app.register_blueprint(views_pagamentos)
