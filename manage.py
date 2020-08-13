from flask import Flask, request, jsonify, make_response
from App.api import *

if __name__ == '__main__':
    app.debug = True
    app.run()