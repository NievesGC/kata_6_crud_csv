from datetime import date
import csv
import os

CURRENCIES = ("EUR","USD")

class Movement:
    def __init__(self,input_date,abstract,amount,currency):
        self.date = input_date
       

        self.abstract = abstract

        self.amount = amount 
        self.currency = currency

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,value):
        self._date = date.fromisoformat(value)
        if self._date > date.today():
            raise ValueError("la fecha debe ser anterior al dia de hoy")
        

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self,value):
        self._amount = float(value)
        if self._amount == 0:
            raise ValueError("la cantidad debe ser posiva o negativa")
        #self._amount = value

    @property
    def currency(self):
        return self._currency
    
    @currency.setter
    def currency(self,value):
        self._currency =  value
        if self._currency not in CURRENCIES:
            raise ValueError(f"currency must be in {CURRENCIES}")
    
    def __eq__(self,other):
        return self.date == other.date and self.abstract == other.abstract and self.amount == other.amount and self.currency == other.currency

class MovementDAO:
    def __init__(self,file_path):
        self.path = file_path
        if not os.path.exists(self.path):
            f = open(file_path, "w")
            f.write("date,abstract,amount,currency\n")

    def insert(self, movement):
        f = open(self.path, "a", newline ="")
        writer = csv.writer(f,delimiter=",", quotechar= '"')
        writer.writerow([movement.date,movement.abstract,
                         movement.amount,movement.currency])
        f.close()

    def all(self):
        f = open(self.path, "r")
        reader = csv.DictReader(f, delimiter= ",", quotechar='"')
        movements = []
        for register in reader:
            m = Movement(register["date"],register["abstract"],register["amount"],register["currency"])
            movements.append(m)
        return movements
    
    def get(self,pos):

        f = open(self.path,"r")
        reader = csv.DictReader(f, delimiter= ",", quotechar='"')
        ix = float("-inf")
        for ix, register in enumerate(reader): #enumerate sirve para... me devuelve una tupla con posicion valor 
            if ix == pos:
                break
        if pos > ix:
            raise IndexError("El movimiento no existe")                
        
        m = Movement(register["date"],register["abstract"],register["amount"],register["currency"])
        return m
    
    def update(self,pos,movement):
        f = open(self.path, "r")
        reader = csv.DictReader(f, delimiter = ",", quotechar="'")
        regs = list(reader) #creamos una lista con todas las lineas del documento
        fieldnames = reader.fieldnames #añadismos las cabeceras
        f.close()
        new_name = "__movements__new.csv" #creamos un nuevo archivo oen el que escribiremos lso datos
        f = open(new_name,"w", newline="")
        writer = csv.DictWriter(f,fieldnames=fieldnames,delimiter = ",", quotechar="'") #esto ya escribe directamente las cabeceras de los datos que he,os creado
        writer.writeheader() #escribe las cabeceras
        writer.writerows(regs[:pos]) 
        writer.writerow({"date":movement.date,"abstract":movement.abstract, #introducimos los datos a capon
                        "amount":movement.amount, "currency":movement.currency})
        writer.writerows(regs[pos+1:])#introducimos los datos desde el principio al anterir 
        f.close()
        os.remove(self.path)
        os.rename(new_name,self.path)#con os borramos el archivo y lo renombramos