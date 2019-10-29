from peewee import *
from basemodel import *
import os

class Rota(Model):
    locSaida = CharField()
    locChegada = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f"\nROTAS\nSaída: {self.locSaida}\nDestino: {self.locChegada}"

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Rota])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit() 

    rota = {
        'locSaida': str(input("Local de saída: ")),
        'locChegada': str(input("Destino: ")),
    }

    minhas_classes = []
    minhas_classes.append(Rota.create(**rota))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()

