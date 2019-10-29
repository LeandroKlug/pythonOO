from peewee import *
from basemodel import *
from empresa import *
import os

class Usuario(Model):
    nomeUsu = CharField()
    cpf = CharField()
    empresa = ForeignKeyField(Empresa, backref="usuario")
    
    class Meta:
        database = db

    def __str__(self):
        return f"\nUSUARIO\nNome: {self.nomeUsu}\nCPF: {self.cpf}"

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Usuario])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit() 

    usuario = {
        'nomeUsu': str(input("Digite seu nome: ")),
        'cpf'    : str(input("Agora, o seu CPF:  ")),
    }    

    minhas_classes = []
    minhas_classes.append(Usuario.create(**usuario, empresa = minhas_classes[0]))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save() 