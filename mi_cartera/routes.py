from mi_cartera import app
from mi_cartera.models import Movement, MovementDAOsqlite
from flask import render_template, request, redirect, flash,url_for
from mi_cartera.forms import MovementsForm
import csv


dao = MovementDAOsqlite("data/movements.db")

@app.route("/")  #crear la ruta
def index():
    try:
        
        return render_template("index.html",the_movements=dao.get_all(), title = "Todos") #necesitamos el render templates(jinya) para llamr a midoc html pero tiene que estar dentro de la carperta templates que debe de estar dentro de la carpeta mi cartera. si no no va 
    except ValueError as e:
        flash("Su fichero de datos esta corrupto")
        flash(str(e))
        return render_template("index.html",the_movementes=[],title = "Todos")

@app.route("/new_movement", methods=["GET","POST"])
def new_mov():
    form = MovementsForm()
    if request.method == "GET":
        return render_template("new.html",the_form=form, title = "Alta de movimiento")
    else:
        if form.validate():
            try:
                dao.insert(Movement(str(form.date.data),form.abstract.data,form.amount.data,form.currency.data))
                return redirect("/")
            except ValueError as e: #lo hacemos con un mensaje flask -- as e es para llamar a ValueError e
                flash(str(e))  #utilizamos el o bjeto flash de flask para convertir en el error en str 
                return render_template("new.html", the_form=form, title = "Alta de moviento")
        else: 
            return render_template("new.html", the_form=form, title = "Alta de moviento")

@app.route("/update_movement/<int:pos>", methods=["GET","POST"])   #int(porque es un numero) id le metes el tipo de variable que quieres meter - le indicas el id
def upd_mov(pos):
    if request.method == "GET":
        mov = dao.get(pos)
        if mov:            
            return render_template("update.html", title="Modificacion de movimiento", the_form=mov,pos=pos )  
        else:
            flash(f"Registro{pos} inexistente")
            return redirect(url_for("index")) #tambien podemos invocarle redirect("/")
    else:
        data= request.form
        try:
            mv = Movement(data["date"],data["abstract"],data["amount"],data["currency"])
            dao.update(pos,mv)
            return redirect(url_for("index"))
        except ValueError as e:
            flash(str(e))
            return render_template("update.html", title="Modificacion de movimiento", the_form=data )