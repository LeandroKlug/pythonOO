from peewee import *
from basemodel import *
from usuario import *
from empresa import * 
from datetime import datetime
import os

class Evento(BaseModel):
    locEvento = CharField()
    nomeEvento = CharField()
    dataEvento = DateField()
    empresa = ForeignKeyField(Empresa)
    usuario = ForeignKeyField(Usuario)

    def __str__(self):
 
        return f"\nEVENTO\nNome evento: {self.nomeEvento}\nLocal evento: {self.locEvento}\nData evento: {self.dataEvento}{self.usuario}" 

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Evento, Empresa, Usuario])

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

    evento = Evento.create(locEvento="São Paulo", nomeEvento="E-commerce Brasil", dataEvento="12/12/2019", empresa = empresa1, usuario = usuario1)
    evento = Evento.create(locEvento="Florianopolis", nomeEvento="TDC", dataEvento="03/05/2019", empresa = empresa2, usuario = usuario2)

    minhas_classes = Evento.select()

    for objeto in minhas_classes:
        print(objeto)  
        print('--------------------')  