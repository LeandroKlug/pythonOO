from peewee import *
from basemodel import *
import os

class Empresa(BaseModel):
    nomeEmp = CharField()
    endEmp = CharField()
    telEmp = IntegerField()
  
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

    empresa1 = Empresa.create(nomeEmp="bla", endEmp="bla", telEmp="1111")
    empresa2 = Empresa.create(nomeEmp="bla1", endEmp="bla1", telEmp="2222")
    empresa3 = Empresa.create(nomeEmp="bla2", endEmp="bla2", telEmp="3333")
    empresa4 = Empresa.create(nomeEmp="bla3", endEmp="bla3", telEmp="4444")
    empresa5 = Empresa.create(nomeEmp="bla4", endEmp="bla4", telEmp="5555")

    minhas_classes = Empresa.select()

    for objeto in minhas_classes:
        print(objeto)
