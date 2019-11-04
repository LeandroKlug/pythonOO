from peewee import *
from basemodel import *
from transporte import *
import os

class Rota(BaseModel):
    locSaida = CharField()
    locChegada = CharField()
    transporte = ForeignKeyField(Transporte)

    def __str__(self):
        return f"\nROTAS\nSaída: {self.locSaida}\nDestino: {self.locChegada}{self.transporte}"

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Rota, Transporte])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit() 

    transporte1 = Transporte.create(tipTrans="Carro", alugado="Sim")
    transporte2 = Transporte.create(tipTrans="Avião", alugado="Não")
    transporte3 = Transporte.create(tipTrans="Moto", alugado="Não")

    rota1 = Rota.create(locSaida="Blumenau", locChegada="Florianopolis", transporte = transporte1)
    rota2 = Rota.create(locSaida="Blumenau", locChegada="São Paulo", transporte = transporte2)
    rota3 = Rota.create(locSaida="Blumenau", locChegada="Minas Gerais", transporte = transporte3)


    minhas_classes = Rota.select()

    for objeto in minhas_classes:
        print(objeto)  
        print('--------------------')  
