from peewee import *
from basemodel import *
from datetime import datetime
import os

class Alimentacao(Model):
    locAlim = CharField()
    nomeLocAlim = CharField()
    dataAlim = DateField()
    qtdAlim = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f"\nALIMENTAÇÃO\nNome restaurante: {self.nomeLocAlim}\nEndereço restaurante: {self.locAlim}\nData refeição: {self.dataAlim}\nQuantidade de refeições: {self.qtdAlim}" 

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Alimentacao])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit()      

    alimentacao = {
        'locAlim': str(input("Local do restaurante: ")),
        'nomeLocAlim': str(input("Nome do restaurante: ")),
        'dataAlim': datetime.strptime(str(input("Data da refeição: (DD/MM/AAAA): ")), "%d/%m/%Y").date(),
        'qtdAlim': int(input("Quantas refeições feitas: ")),
    }  

    minhas_classes = []
    minhas_classes.append(Alimentacao.create(**alimentacao))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()