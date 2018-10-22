"""Testing crud."""
from pet import db
from pet.models import Cliente, Cachorro, Contato, Endereco, Venda

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

Cliente.query.all()
Cachorro.query.all()

Cliente.query.get(1).nome
Cliente.query.filter_by(nome='Aline').first()


# query = db.session.query(Cliente).order_by(Cliente.id)
# for _row in query.all():
#     print(_row.nome, _row.id)

## create cachorro

def get_id(termo):
    # query = db.session.query(Cliente).filter_by(nome=nome).all()
    dono = db.session.query(Cliente).filter(Cliente.nome.ilike(termo)).first()
    return dono.id

get_id('aline')


puka = Cachorro('Puka', 'shitzu', 'longo', datetime(2014, 3, 1),
                datetime(2016, 10, 1), 'F', 'S')

# db.session.add(new)
# db.session.commit()
# db.session.rollback()
# cachorro.query.all()
# cachorro.query.get(1)
# cachorro.query.filter(cachorro.nome.ilike('puka')).first()

aline = Cliente.query.filter_by(nome='Aline').first()

aline.cachorro.append(puka)
# aline.cachorro.remove(puka)
db.session.add(aline)
# db.session.commit()
###

kate = Cachorro('Kate', 'shitzu', 'longo', datetime(2013, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

neg = Cachorro('Neguinha', 'shitzu', 'longo', datetime(2014, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

sansa = Cachorro('Sansa', 'spitz', 'longo', datetime(2015, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

amanda = Cliente.query.filter(Cliente.nome.ilike('amanda')).first()

amanda.cachorro.extend([sansa, kate, neg])

# db.session.add(amanda)
# db.session.commit()

###

pipoca = Cachorro('pipoca', 'mascara', 'curto', datetime(2010, 10, 14),
                    datetime(2018, 10, 14), 'F', 'S')
leon = Cachorro('Leon', 'bull-terrier', 'longo', datetime(2009, 10, 14),
                    datetime(2018, 10, 14), 'M', 'S')

marcelo = Cliente('Marcelo', 'M')
marcelo.cachorro.extend([pipoca, leon])
db.session.add_all([marcelo, amanda, aline])
db.session.commit()

###
Cachorro.query.all()
Cliente.query.all()

# Cliente.query.delete()
# cachorro.query.delete()

for class_instance in db.session.query(cachorro).all():
    print(vars(class_instance))


import pandas as pd

# mostra tabela de cachorros
df = pd.read_sql(
    db.session.query(cachorro).filter(cachorro.id < 100).statement,
    db.session.bind)

df

# mostra todas as colunas
query = db.session.query(Cliente, cachorro).join(cachorro)

# mostra o nome do dono e do cachorro
query = db.session.query(
    Cliente.nome.label("Cliente"),
    cachorro.nome.label("dog"),
    cachorro.breed.label('raça'),
    cachorro.nascimento.label('nascimento')
    ).join(cachorro)


# retorna resultado em tuplas
for item in query.all():
    print(item)

# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
