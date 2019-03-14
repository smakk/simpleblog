from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['connect'] = app.config['DATABASETYPE']+r'+'+app.config['DBDRIVER']+\
                                        r'://'+app.config['DBUSER']+r':'+app.config['DBPASSWORD']+\
                                        r'@'+app.config['DBADRESS']+r':'+app.config['DBPORT']+r'/'+\
                                        app.config['DATABASE']

from api_1 import myapi_1
app.register_blueprint(myapi_1)

import myapp.db_operations
import myapp.view