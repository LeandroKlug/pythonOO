from peewee import *
from basemodel import *
import os

class Empresa(Model):
    nomeEmp = CharField()
    endEmp = CharField()
    telEmp = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f"\nEMPRESA\nEmpresa: {self.nomeEmp}\nEndereço {self.endEmp}\nTelefone: {str(self.telEmp)}"

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Empresa])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit()

    empresa = {
        'nomeEmp': str(input("Digite sua empresa: ")),
        'endEmp' : str(input("O endereço da sua empresa: ")),
        'telEmp' : int(input("O telefone da sua empresa: "))
    }

    minhas_classes = []
    minhas_classes.append(Empresa.create(**empresa))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()    