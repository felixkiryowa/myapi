import flask
APP=flask.Flask(__name__)
APP.config["DEBUG"]=True
from api import *
if __name__ == '__main__':
    APP.run()