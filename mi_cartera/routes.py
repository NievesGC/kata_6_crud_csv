from mi_cartera import app
from mi_cartera.models import Movement, MovementDAO
from flask import render_template, request, redirect, flash,url_for
import csv

dao = MovementDAO("movements.dat")

@app.route("/")  #crear la ruta
def index():
    try:
        return render_template("index.html",the_movements=dao.all(), title = "Todos") #necesitamos el render templates(jinya) para llamr a midoc html pero tiene que estar dentro de la carperta templates que debe de estar dentro de la carpeta mi cartera. si no no va 
    except ValueError as e:
        flash(str(e))
        return render_template("index.html",the_movementes=[],title = "Todos")

@app.route("/new_movement", methods=["GET","POST"])
def new_mov():
    if request.method == "GET":
        return render_template("new.html",the_form={}, title = "Alta de movimiento")
    else:
        data = request.form
        try:
            dao.insert(Movement(data["date"],data["abstract"],
                                  data["amount"],data["currency"]))
            return redirect("/")
        except ValueError as e: #lo hacemos con un mensaje flask -- as e es para llamar a ValueError e
            flash(str(e))  #utilizamos el o bjeto flash de flask para convertir en el error en str 
            return render_template("new.html", the_form=data, title = "Alta de moviento")

@app.route("/update_movement/<int:pos>", methods=["GET","POST"])   #int(porque es un numero) id le metes el tipo de variable que quieres meter - le indicas el id
def upd_mov(pos):
    if request.method == "GET":
        mov = dao.get(pos)
        return render_template("update.html", title="Modificacion de movimiento", the_form=mov,pos=pos )  
    else:
        data= request.form
        try:
            mv = Movement(data["date"],data["abstract"],data["amount"],data["currency"])
            dao.update(pos,mv)
            return redirect(url_for("index"))
        except ValueError as e:
            flash(str(e))
            return render_template("update.html", title="Modificacion de movimiento", the_form=data )