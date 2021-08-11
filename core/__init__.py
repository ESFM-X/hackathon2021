### Flask 
from flask import Flask
from flask_wtf.csrf import CSRFProtect

### Built-in
import os
from os import environ
### Local
from . import config

#### App config
SECRET_KEY = os.urandom(32)
app = Flask(__name__,  static_folder='../static', template_folder = '../templates')
csrf = CSRFProtect(app)

environment = environ.get("FLASK_ENV", default="development")

if environment == "development":
   print('\n\nTHIS IS A DEVELOPMENT ENVIRONMENT \n\n')
   cfg = config.DevelopmentConfig()
elif environment == "production":
   print('\n\nTHIS IS A DEVELOPMENT PRODUCTION \n\n')
   cfg = config.ProductionConfig()
 
app.config.from_object(cfg)
app.config['SECRET_KEY'] = SECRET_KEY

import views