from flask import Blueprint

galeriecv = Blueprint('galeriecv', __name__, template_folder='templates', static_folder='static')

from . import routes


