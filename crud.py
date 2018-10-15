"""Testing crud."""
from pet import db
from pet.models import cliente, cachorro
from datetime import datetime



## create cliente
db.create_all()
# db.session.remove()
aline = cliente('Aline', 'M')
julio = cliente('Júlio', 'H')
amanda = cliente('Amanda', 'M')

db.session.add_all([aline, julio, amanda])

db.session.commit()
# db.session.rollback()

## read cliente

cliente.query.all()
cachorro.query.all()

cliente.query.get(1).nome
cliente.query.filter_by(nome='Aline').first()


# query = db.session.query(cliente).order_by(cliente.id)
# for _row in query.all():
#     print(_row.nome, _row.id)

## create cachorro

def get_id(termo):
    # query = db.session.query(cliente).filter_by(nome=nome).all()
    dono = db.session.query(cliente).filter(cliente.nome.ilike(termo)).first()
    return dono.id

get_id('aline')


puka = cachorro('Puka', 'shitzu', 'longo', datetime(2014, 3, 1),
                datetime(2016, 10, 1), 'F', 'S')

# db.session.add(new)
# db.session.commit()
# db.session.rollback()
# cachorro.query.all()
# cachorro.query.get(1)
# cachorro.query.filter(cachorro.nome.ilike('puka')).first()

aline = cliente.query.filter_by(nome='Aline').first()

aline.cachorro.append(puka)
# aline.cachorro.remove(puka)
db.session.add(aline)
# db.session.commit()
###

kate = cachorro('Kate', 'shitzu', 'longo', datetime(2013, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

neg = cachorro('Neguinha', 'shitzu', 'longo', datetime(2014, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

sansa = cachorro('Sansa', 'spitz', 'longo', datetime(2015, 10, 10),
                datetime(2016, 10, 10), 'F', 'S')

amanda = cliente.query.filter(cliente.nome.ilike('amanda')).first()

amanda.cachorro.extend([sansa, kate, neg])

# db.session.add(amanda)
# db.session.commit()

###

pipoca = cachorro('pipoca', 'mascara', 'curto', datetime(2010, 10, 14),
                    datetime(2018, 10, 14), 'F', 'S')
leon = cachorro('Leon', 'bull-terrier', 'longo', datetime(2009, 10, 14),
                    datetime(2018, 10, 14), 'M', 'S')

marcelo = cliente('Marcelo', 'M')
marcelo.cachorro.extend([pipoca, leon])
db.session.add_all([marcelo, amanda, aline])
db.session.commit()

###
cachorro.query.all()
cliente.query.all()

cliente.query.delete()
cachorro.query.delete()

for class_instance in db.session.query(cachorro).all():
    print(vars(class_instance))


import pandas as pd

# mostra tabela de cachorros
df = pd.read_sql(
    db.session.query(cachorro).filter(cachorro.id < 100).statement,
    db.session.bind)

df

# mostra todas as colunas
query = db.session.query(cliente, cachorro).join(cachorro)

# mostra o nome do dono e do cachorro
query = db.session.query(
    cliente.nome.label("cliente"),
    cachorro.nome.label("dog"),
    cachorro.breed.label('raça'),
    cachorro.idade.label('idade')
    ).join(cachorro)


# retorna resultado em tuplas
for item in query.all():
    print(item)

# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
