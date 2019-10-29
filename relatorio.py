from peewee import *
from basemodel import *
import os

class Relatorio(Model):
    # Essa classe envia o relatório com todas as informações
    rel = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f"\nRELATORIO\n{self.rel}"

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Relatorio])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit() 

    relatorio = {
        'rel': str(input())
    }

    minhas_classes = []
    minhas_classes.append(Relatorio.create(**relatorio))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()