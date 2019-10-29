from peewee import *
from basemodel import *
from datetime import datetime
import os

class Evento(Model):
    locEvento = CharField()
    nomeEvento = CharField()
    dataEvento = DateField()

    class Meta:
        database = db

    def __str__(self):
        return f"\nEVENTO\nNome evento: {self.nomeEvento}\nLocal evento: {self.locEvento}\nData evento: {self.dataEvento}" 

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Evento])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit() 

    evento = {
        'nomeEvento': str(input("Nome do evento: ")),
        'locEvento': str(input("Local do evento: ")),
        'dataEvento': datetime.strptime(str(input("Data em que vai ocorrer o evento: (DD/MM/AAAA) ")), "%d/%m/%Y").date(),
    }

    minhas_classes = []
    minhas_classes.append(Evento.create(**evento))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()