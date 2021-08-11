import logging

class Config(object):
   def __init__(self):
       logging.basicConfig(level=logging.DEBUG)
 
   DEBUG = False
   TESTING = False
class DevelopmentConfig(Config):
   DEBUG = True
   SECRET_KEY = 'INSECURE_FOR_LOCAL_DEVELOPMENT'
 
class ProductionConfig(Config):
   DEBUG = False
   TESTING = False