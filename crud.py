"""Testing crud."""
from pet import db
from pet.models import cliente, cachorro
from datetime import datetime


## create cliente
db.create_all()

new = cliente('Aline', 'M')
new

db.session.add(new)

new = cliente('Amanda', 'M')
new = cliente('Júlio', 'H')


db.session.commit()
# db.session.rollback()

## read cliente

cliente.query.all()
cliente.query.get(1)
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


new = cachorro('Puka', 'shitzu', 'longo', 4, datetime(2016, 10, 1), 'F', 'S')
new

db.session.add(new)



db.session.commit()
db.session.rollback()


cachorro.query.all()
cachorro.query.get(1)
cachorro.query.filter(cachorro.nome.ilike('puka')).first()

##

# p1 = Parent(name="Alice")
# p2 = Parent(name="Bob")
#
# c1 = Child(name="foo")
# c2 = Child(name="bar")
# c3 = Child(name="ker")
# c4 = Child(name="cat")
#
# p1.children.extend([c1, c2, c3])
# p2.children.append(c4)


aline = cliente.query.filter_by(nome='Aline').first()
aline

puka = cachorro.query.get(1)
puka

aline.cachorro.append(puka)

db.session.add(aline)
db.session.commit()
###

kate = cachorro('Kate', 'shitzu', 'longo', 6, datetime(2016, 10, 10), 'F', 'S')
neg = cachorro('Neguinha', 'shitzu', 'longo', 3, datetime(2016, 10, 10), 'F', 'S')
sansa = cachorro('Sansa', 'spitz', 'longo', 3, datetime(2016, 10, 10), 'F', 'S')

amanda = cliente.query.filter(cliente.nome.ilike('amanda')).first()
amanda

amanda.cachorro.extend([sansa, kate, neg])

db.session.add(amanda)
db.session.commit()

###
cachorro.query.all()

for class_instance in db.session.query(cachorro).all():
    print(vars(class_instance))


import pandas as pd


df = pd.read_sql(db.session.query(cachorro).filter(cachorro.id < 100).statement, db.session.bind)

df


query = db.session.query(cliente, cachorro).join(cachorro)
query = db.session.query(cliente.nome.label("cliente"), cachorro.nome.label("dog")).join(cachorro)


for item in query.all():
    print(item)


df = pd.read_sql(query.statement, db.session.bind)

df
