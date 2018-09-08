import flask
app=flask.Flask(__name__)
app.config["DEBUG"]=True
from api import *
if __name__ == '__main__':
    app.run()