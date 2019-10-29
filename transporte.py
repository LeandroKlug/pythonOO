from peewee import *
from basemodel import *
import os

class Transporte(Model):
    tipTrans = CharField()
    alugado = CharField()

    class Meta:
        database = db

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

    transporte = {
      'tipTrans': str(input('Digite o tipo de transporte utilizado: ')),
      'alugado' : bool(True if str(input("Já está alugado (S/N)? ")).lower() == "s" else False)
    }

    minhas_classes = []
    minhas_classes.append(Transporte.create(**transporte))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save() 
