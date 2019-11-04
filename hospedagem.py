from peewee import *
from basemodel import *
from datetime import datetime
import os

class Hospedagem(BaseModel):
    locHosp = CharField()
    nomeHosp = CharField()
    dataEntrada = DateField()
    dataSaida = DateField()

    def __str__(self):
        return f"\nHOSPEDAGEM\nNome hospedagem: {self.nomeHosp}\nLocal hospedagem: {self.locHosp}\nData entrada: {self.dataEntrada}\nData saída: {self.dataSaida}" 

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Hospedagem])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit()

    hospedagem = {
        'locHosp': str(input("Endereço da hospedagem: ")),
        'nomeHosp': str(input("Nome da hospedagem: ")),
        'dataEntrada': datetime.strptime(str(input("Data do check-in (DD/MM/AAAA): ")), "%d/%m/%Y" ).date(),
        'dataSaida': datetime.strptime(str(input("Data do check-out (DD/MM/AAAA): ")), "%d/%m/%Y").date(),
    } 

    minhas_classes = []
    minhas_classes.append(Hospedagem.create(**hospedagem))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()