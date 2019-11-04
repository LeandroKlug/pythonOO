from peewee import *
from basemodel import *
import os

class Transporte(BaseModel):
    tipTrans = CharField()
    alugado = CharField()

    def __str__(self):
        return f"\nTRANSPORTE\nTransporte: {self.tipTrans}\nAlugado: {self.alugado}" 

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Transporte])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit()

    transporte1 = Transporte.create(tipTrans="Carro", alugado="Sim")
    transporte2 = Transporte.create(tipTrans="Avião", alugado="Não")
    transporte3 = Transporte.create(tipTrans="Moto", alugado="Não")

    minhas_classes = Transporte.select()

    for objeto in minhas_classes:
        print(objeto)  
        print('--------------------')  
