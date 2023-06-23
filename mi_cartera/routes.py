from mi_cartera import app
from flask import render_template, request, redirect
import csv

@app.route("/")  #crear la ruta
def index():
    f = open("movements.dat","r")                         #se pondra todo esto para importarlo directamente desde archivos de texto sin tener que p onerlo todo en html esto e sun modulo CSV
    reader = csv.DictReader(f, delimiter=",", quotechar='"')
    movements = list(reader)
    
    return render_template("index.html",the_movements=movements) #necesitamos el render templates(jinya) para llamr a midoc html pero tiene que estar dentro de la carperta templates que debe de estar dentro de la carpeta mi cartera. si no no va 

@app.route("/new_movement", methods=["GET","POST"])
def new_mov():
    if request.method == "GET":
        return render_template("new.html")
    else:
        data = request.form
        f = open("movements.dat","a")
        writer = csv.DictWriter(f,fieldnames=data.keys())
        writer.writerow(data)
        f.close()

        return redirect("/")