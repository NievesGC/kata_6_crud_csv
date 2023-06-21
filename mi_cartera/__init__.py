from flask import Flask, render_template #funcion de flask
import csv

app = Flask(__name__) #asi se crea la app

@app.route("/")  #crear la ruta
def index():
    f = open("movements.dat","r")                         #se pondra todo esto para importarlo directamente desde archivos de texto sin tener que p onerlo todo en html esto e sun modulo CSV
    reader = csv.reader(f, delimiter=",", quotechar=" ")
    movements = list(reader)
    return render_template("index.html",the_movements=movements) #necesitamos el render templates para llamr a midoc html pero tiene que estar dentro de la carperta templates que debe de estar dentro de la carpeta mi cartera. si no no va 



