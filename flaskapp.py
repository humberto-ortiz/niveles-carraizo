import os
import pygal
from datetime import datetime, timedelta
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory, make_response

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

@app.route("/niveles")
def niveles():
    return send_from_directory("static/", "niveles.txt")

@app.route("/plot")
def plot():
    datey = pygal.DateY(x_label_rotation=20)
    datey.add("Visits", [
    (datetime(2013, 1, 2), 300),
    (datetime(2013, 1, 12), 412),
    (datetime(2013, 2, 2), 823),
    (datetime(2013, 2, 22), 672)
    ])
    return make_response(datey.render())

if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])
