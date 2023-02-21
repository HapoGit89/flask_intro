# Put your app in here.
""" creates flask routes using math operators"""

from flask import Flask, request

from operations import *

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{add(a,b)}"

@app.route('/sub')
def subt():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{sub(a,b)}"

@app.route('/mult')
def multi():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{mult(a,b)}"

@app.route('/div')
def divi():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{div(a,b)}"
