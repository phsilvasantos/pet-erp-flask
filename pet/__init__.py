from flask import Flask
from pet.core.views import core


app = Flask(__name__)

# BLUEPRINT CONFIGS #######

# We've imported them here for easy reference

app.register_blueprint(core)
