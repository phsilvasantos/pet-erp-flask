"""Testing crud."""
from petshop import db
from petshop.models import *

from datetime import datetime
import pandas as pd



## create Cliente
db.create_all()
# db.session.remove()
aline = Cliente('Aline', 'M')
julio = Cliente('Júlio', 'H')
amanda = Cliente('Amanda', 'M')

db.session.add_all([aline, julio, amanda])

db.session.commit()
# db.session.rollback()

## read Cliente

Clientes.query.all()
Peludos.query.all()

teste = Clientes.query.get(1)
teste
Cliente.query.filter_by(nome='Aline').first()


# query = db.session.query(Cliente).order_by(Cliente.id)
# for _row in query.all():
#     print(_row.nome, _row.id)

## create peludo

def get_id(termo):
    # query = db.session.query(Cliente).filter_by(nome=nome).all()
    dono = db.session.query(Cliente).filter(Cliente.nome.ilike(termo)).first()
    return dono.id

get_id('aline')


puka = Peludo('Puka', 'shitzu', 'longo', datetime(2014, 3, 1),
                datetime(2016, 10, 1), 'F', 'S')

# db.session.add(new)
# db.session.commit()
# db.session.rollback()
# peludo.query.all()
# peludo.query.get(1)
# peludo.query.filter(peludo.nome.ilike('puka')).first()

aline = Cliente.query.filter_by(nome='Aline').first()

aline.peludo.append(puka)
# aline.peludo.remove(puka)
db.session.add(aline)
# db.session.commit()
###

kate = Peludo('Kate', 'shitzu', 'longo', datetime(2013, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

neg = Peludo('Neguinha', 'shitzu', 'longo', datetime(2014, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

sansa = Peludo('Sansa', 'spitz', 'longo', datetime(2015, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

amanda = Cliente.query.filter(Cliente.nome.ilike('amanda')).first()

amanda.peludo.extend([sansa, kate, neg])

# db.session.add(amanda)
# db.session.commit()

###

pipoca = Peludo('pipoca', 'mascara', 'curto', datetime(2010, 10, 14),
                    datetime(2018, 10, 14), 'F', 'S')
leon = Peludo('Leon', 'bull-terrier', 'longo', datetime(2009, 10, 14),
                    datetime(2018, 10, 14), 'M', 'S')

marcelo = Cliente('Marcelo', 'M')
marcelo.peludo.extend([pipoca, leon])
db.session.add_all([marcelo, amanda, aline])
db.session.commit()

###
Peludo.query.all()
Cliente.query.all()

# Cliente.query.delete()
# peludo.query.delete()

for class_instance in db.session.query(peludo).all():
    print(vars(class_instance))


import pandas as pd

# mostra tabela de peludos
df = pd.read_sql(
    db.session.query(peludo).filter(peludo.id < 100).statement,
    db.session.bind)

df

# mostra todas as colunas
query = db.session.query(Cliente, peludo).join(peludo)

# mostra o nome do dono e do peludo
query = db.session.query(
    Cliente.nome.label("Cliente"),
    peludo.nome.label("dog"),
    peludo.breed.label('raça'),
    peludo.nascimento.label('nascimento')
    ).join(peludo)


# retorna resultado em tuplas
for item in query.all():
    print(item)

# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
