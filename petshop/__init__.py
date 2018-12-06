"""application configuration."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import secrets
import os


application = Flask(__name__)
Bootstrap(application)
application.config['SECRET_KEY'] = secrets.key

login_manager = LoginManager()
# BLUEPRINT CONFIGS #######

# DB Config
basedir = os.path.abspath(os.path.dirname(__file__))
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)
Migrate(application, db)


from petshop.views.views_cadastros import views_cadastros
from petshop.views.views_consultas import views_consultas
from petshop.views.views_vendas import views_vendas
from petshop.views.views_pagamentos import views_pagamentos

application.register_blueprint(views_cadastros)
application.register_blueprint(views_consultas)
application.register_blueprint(views_vendas)
application.register_blueprint(views_pagamentos)


# Login manager config
login_manager.init_app(application)
login_manager.login_view = 'views_cadastros.login'
