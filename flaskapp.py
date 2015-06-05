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
    niveles = []
    with open("static/niveles.txt","r") as f:
        for line in f:
            fields = line.split()
            niveles.append( ( datetime.strptime(fields[0], "%Y-%m-%d"), float(fields[1]) ) )
    start, trash = niveles[0]
    end, trash = niveles[-1]
    datey = pygal.DateY(x_label_rotation=20,range=(30.0,41.14),title=u'Niveles')
    datey.x_label_format = "%Y-%m-%d"
    datey.add("Carraizo", niveles)
    datey.add("Optimo", [(start, 41.14), (end, 41.14)])
    datey.add("Observacion", [(start, 39.5), (end, 39.5)])
    datey.add("Ajustes", [(start, 38.5), (end, 38.5)])
    datey.add("Control", [(start, 36.5), (end, 36.5)])
    return datey.render_response()

if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])
