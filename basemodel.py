from peewee import *

arq = 'viagem.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db