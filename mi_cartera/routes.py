from mi_cartera import app
from mi_cartera.models import Movement, MovementDAO
from flask import render_template, request, redirect
import csv

dao = MovementDAO("movements.dat")

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
        """
        nuevo_mov = MovementDAO("movements.dat")
        """
        data = request.form
        dao.insert(Movement(data["date"],data["abstract"],
                                  data["amount"], data["currency"]))
        """
        f = open("movements.dat","a", newline="")               #NEWLINE SIRVE PARA CUANDO SE AÑADEN LAS LINEAS EN MOVEMENTS QUE NO SE QUEDE UNE SPACIO ENTRE ELLAS
        writer = csv.DictWriter(f,fieldnames=data.keys())
        writer.writerow(data)
        f.close()
        """
        return redirect("/")