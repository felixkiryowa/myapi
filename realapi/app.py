"""
This is the main module

"""
import flask
from api_urls import GetApiUrls
APP = flask.Flask(__name__)
APP.env = 'development'
APP.testing = True
GetApiUrls.get_all_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)
