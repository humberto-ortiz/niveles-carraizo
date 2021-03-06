# coding: utf-8
import os
import pygal
from random import randint, shuffle
from datetime import datetime, timedelta
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory, make_response

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

data_dir = app.config['DATA_DIR']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/random")
def rand():
    students = [#"Dorian Baez",
                #"Manuel Chau",
                #"Julio Torres",
                'Alfredo Valles Salas',
                #'Omar Cruz',
                'Christian	Agostini',
                'Jeffrey	Chan',
                'Kai-Ming	Chow',
                'Omar	Cruz Pantoja',
                'Ian	Davila',
                'Alejandro 	Deloach',
                'Robbin	Díaz',
                'Israel	Dilan',
                'Julio	Franco',
                'Louis	Gil',
                'Lillian	Gonzalez',
                'María Margarita	López-Delgado',
                'Christian	Maldonado',
                'Luis	Morales',
                #'Emmanuel	Nieves',
                'José	Reyes',
                'Anthony	Rios',
                'Grace M.	Rodriguez',
                'Kristyan	Rodriguez',
                'Javier	Rodriguez Ramos',
                'Omar	Rosado',
                'Matias	Rosner',
                'Andres	Sanjurjo',
                'Valerie	Santiago']
    shuffle(students)
    return "<li>" + "\n<li>".join(students)#[randint(0,len(students)-1)]

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

@app.route("/niveles")
def niveles():
    return send_from_directory(data_dir, "niveles.txt")

@app.route("/plot")
def plot():
    niveles = []
    with open(data_dir + "/niveles.txt","r") as f:
        for line in f:
            fields = line.split()
            if 10 == len(fields[0]):
                fmt = "%Y-%m-%d"
            else:
                fmt =  "%Y-%m-%dT%H:%M:%S"
                fields[0] = fields[0][:-6]

            niveles.append (( datetime.strptime(fields[0], fmt), float(fields[1]) ) )
    if len(niveles) > 30:
        limit = -30 # where should we start plotting set to -30 for one month's data
    else:
        limit = 0
    start, trash = niveles[limit]
    end, trash = niveles[-1]
    datey = pygal.DateY(x_label_rotation=20,range=(30.0,41.14),title=u'Niveles',
    y_title="Metros sobre el nivel del mar")
    # Can't fix label format, this doesn't work.
    datey.x_label_format = "%Y-%m-%d"
    datey.add("Carraizo", niveles[limit:])
    datey.add("Optimo", [(start, 41.14), (end, 41.14)])
    datey.add("Observacion", [(start, 39.5), (end, 39.5)])
    datey.add("Ajustes", [(start, 38.5), (end, 38.5)])
    datey.add("Control", [(start, 36.5), (end, 36.5)])
    datey.add("Fuera de servicio", [(start, 30.0), (end, 30.0)])
    # pygal can render flask response directly
    return datey.render_response()

@app.route("/plotall")
def plotall():
    niveles = []
    with open(data_dir + "/niveles.txt","r") as f:
        for line in f:
            fields = line.split()
            niveles.append( ( datetime.strptime(fields[0], "%Y-%m-%d"), float(fields[1]) ) )

    start, trash = niveles[0]
    end, trash = niveles[-1]
    datey = pygal.DateY(x_label_rotation=20,range=(30.0,41.14),title=u'Niveles',
    y_title="Metros sobre el nivel del mar")
    # Can't fix label format, this doesn't work.
    datey.x_label_format = "%Y-%m-%d"
    datey.add("Carraizo", niveles)
    datey.add("Optimo", [(start, 41.14), (end, 41.14)])
    datey.add("Observacion", [(start, 39.5), (end, 39.5)])
    datey.add("Ajustes", [(start, 38.5), (end, 38.5)])
    datey.add("Control", [(start, 36.5), (end, 36.5)])
    datey.add("Fuera de servicio", [(start, 30.0), (end, 30.0)])
    # pygal can render flask response directly
    return datey.render_response()

if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])
