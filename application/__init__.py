from flask import Flask
from .galeriecv import galeriecv
from .home import home
from .picture import picture
import os

app = Flask(__name__)

app.config.from_pyfile('config/configuration.cfg')
app.register_blueprint(home)
app.register_blueprint(picture)
app.register_blueprint(galeriecv)
