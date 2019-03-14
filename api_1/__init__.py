from flask.blueprints import Blueprint
from flask.templating import render_template
from flask.globals import current_app


myapi_1 = Blueprint('myapi_1',__name__,url_prefix='/api_1')

@myapi_1.route('/')
def api_1_test():
    return current_app.config['ROOTUSER']