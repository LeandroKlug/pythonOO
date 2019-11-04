from peewee import *
from basemodel import *
import os

class Pagamento(BaseModel):
    metPag = CharField()
    valor = FloatField()
    nf = IntegerField()

    def __str__(self):
        return f"\nPAGAMENTO\nMétodo pagamento: {self.metPag}\nValor: R${self.valor:.2f}\nNota fiscal: {self.nf}" 

if __name__ == '__main__':

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Pagamento])

    except OperationalError as e:
        print('Erro ao criar tabelas:'+ str(e))
        exit() 

    pagamento = {
        'metPag': str(input("Meio de pagamento: ")),
        'valor': float(input("Valor á pagar: ")),
        'nf': int(input("Insira o número da nota fiscal: ")),
    }

    minhas_classes = []
    minhas_classes.append(Pagamento.create(**pagamento))

    for objeto in minhas_classes:
        print(objeto)
        # objeto.save()