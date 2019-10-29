from peewee import *
from basemodel import *
import os

class Viagem(Model):
    # Essa classe engloba todas outras classes
    # Gerando um relatório final para envio por e-mail
    trip = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f"\nVIAGEM\n{self.trip}" 

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Viagem])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit()  

    viagem = {
        'trip': str(input()),
    }

    minhas_classes = []
    minhas_classes.append(Viagem.create(**viagem))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()