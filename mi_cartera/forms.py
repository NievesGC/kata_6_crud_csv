from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length 
#crear formulario de alta 
class MovementsForm(FlaskForm):
    date = DateField("Fecha", validators=[DataRequired("La fecha es obligatoria")])
    #hay quie decirle  que es de tipo fecha con Field hay para mas cosas, VALIDATORS INSTANCIA DATAREQUIRED 
    abstract = StringField("Concepto", validators = [DataRequired("Concepto obligatorio"), Length(min=5)])
    # stringfield indica que e sun texto, el length le pone sla longitud minima, se le podria añadir un mensaje que lo indicara ¿como?
    amount = FloatField("Cantidad", validators = [DataRequired("Cantidad obligatoria")])
    #le indicamo que es uno numero, como no existe validador de + o - lo tendremos que crear 
    currency = SelectField("Moneda", validators=[DataRequired("Moneda obligatoria")], choices=[("EUR","Euros"),("USD","Dólares americanos")])
    #le decimos que es ¿selct que es ¿?moendad?, en choices le metemos una lista de tupas con la clave valor


    submit = SubmitField("Enviar")
    #para crear el boton de validar, no necesita validadores, se hace clic y lo lanza 
