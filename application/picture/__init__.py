from flask import Blueprint

picture = Blueprint('picture', __name__, template_folder='templates', static_folder='static')

from . import routes



