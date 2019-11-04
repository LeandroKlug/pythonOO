from peewee import *
from basemodel import *
from empresa import *
import os

class Usuario(BaseModel):
    nomeUsu = CharField()
    cpf = CharField()
    empresa = ForeignKeyField(Empresa)

    def __str__(self):
        return f"\nUSUARIO\nNome: {self.nomeUsu}\nCPF: {self.cpf}{self.empresa}"

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Usuario, Empresa])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit() 

    empresa1 = Empresa.create(nomeEmp="bla1", endEmp="bla1", telEmp="2222")
    empresa2 = Empresa.create(nomeEmp="bla2", endEmp="bla2", telEmp="3333")
    empresa3 = Empresa.create(nomeEmp="bla3", endEmp="bla3", telEmp="4444")
    empresa4 = Empresa.create(nomeEmp="bla4", endEmp="bla4", telEmp="5555")

    usuario1 = Usuario.create(nomeUsu="João", cpf="000000", empresa=empresa1)
    usuario2 = Usuario.create(nomeUsu="José", cpf="111111", empresa=empresa2)
    usuario3 = Usuario.create(nomeUsu="Mauricio", cpf="22222", empresa=empresa3)
    usuario4 = Usuario.create(nomeUsu="Bartolomeu", cpf="333333", empresa=empresa4)

    minhas_classes = Usuario.select()

    for objeto in minhas_classes:
        print(objeto)  
        print('--------------------')  
