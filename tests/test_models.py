from datetime import date
from mi_cartera.models import Movement, MovementDAO
import pytest
import os
import csv
def test_create_movements():
    m = Movement("0002-01-31","Sueldo", 1000, "EUR")
    assert m.date == date(2,1,31)
    assert m.abstract == "Sueldo"
    assert m.amount == 1000
    assert m.currency == "EUR"

def test_fails_of_date_greater_than_today():
    with pytest.raises(ValueError):
        m = Movement ("9999-12-31","concepto",1000,"USD")

def test_change_date():
    m = Movement("0002-01-31","Sueldo", 1000, "EUR")
    m.date = "1970-04-08"
    assert m.date == date(1970,4,8)
    

def test_fails_if_aomunt_eq__zero():
    pass

def test_fails_if_currency_not_in_currency():
    pass
def test_fails_if_change_currencyy_not_in_currencies():
    pass

def test_create_dao():
    path = "cuadreno_de_mentira.dat"
    if os.path.exists(path):
        os.remove(path)
   
    dao = MovementDAO(path)
   
    f = open(path,"r")
    cabecera = f.readline()

    assert cabecera == "date,abstract,amount,currency\n"

def test_insrance_dao_path_exists():
    path = "cuadreno_de_mentira.dat"
    if os.path.exists(path):
        os.remove(path)
   
    dao = MovementDAO(path)
    dao.insert(Movement("0001-01-01","Concept",12,"EUR"))
    dao = MovementDAO(path)
    dao.insert(Movement("0001-01-02","Concept",122,"EUR"))
    

    f = open(path,"r")
    reader = csv.reader(f,delimiter=",", quotechar='"')
    data = list(reader)

    assert len(data) == 3 

def test_instert_one_movement():
    path = "cuadreno_de_mentira.dat"
    if os.path.exists(path):
        os.remove(path)
   
    dao = MovementDAO(path)
    mvm = Movement("2023-01-01","Un concepto",1,"EUR")
    dao.insert(mvm)

    f = open(path,"r")
    reader = csv.reader(f, delimiter = ",",quotechar='"')
    registros = list(reader)

    assert registros[0] == ["date","abstract","amount","currency"]
    assert registros[1] == ["2023-01-01","Un concepto","1","EUR"]

def all(self):
    pass
    #devolver un alista de Movements con todos los registros del fichero