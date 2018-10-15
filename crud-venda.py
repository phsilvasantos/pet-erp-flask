"""Testing crud."""
from pet import db
from pet.models import cliente, cachorro, venda, contato, endereco
from datetime import datetime
import pandas as pd

# db.metadata.clear()
# db.create_all()


cliente.query.all()

aline = cliente.query.filter_by(nome='Aline').first()
puka = cachorro.query.filter_by(nome='Puka').first()

sale = venda(
        descricao='tosa na tesoura', data_venda=datetime(2018, 10, 12),
        valor_venda=100, valor_taxi=10, n_banhos=1, tipo='avulso',
        pacote='---', forma_pagto='cash', data_pagto=datetime(2018,10,12),
        valor_entrada=110
        )

aline.venda.append(sale)
puka.venda.append(sale)

####
comprador = cliente.query.filter(cliente.nome.ilike('marcelo')).first()
cao = cachorro.query.filter(cachorro.nome.ilike('leon')).first()

sale = venda(
        descricao='tosa na maquina', data_venda=datetime(2018, 9, 12),
        valor_venda=50, valor_taxi=10, n_banhos=1, tipo='avulso',
        pacote='---', forma_pagto='cash', data_pagto=datetime(2018, 9, 12),
        valor_entrada=60
        )

comprador.venda.append(sale)
cao.venda.append(sale)

db.session.add_all([aline, puka, comprador, cao])
db.session.commit()


# mostra o nome do dono e do cachorro
query = db.session.query(
    cliente.nome.label("cliente"),
    cachorro.nome.label("dog"),
    cachorro.breed.label('raça'),
    venda.data_venda.label('data'),
    venda.valor_entrada.label('valor'),
    venda.descricao
    ).join(cachorro, venda)


help(db.session.query().join)
# retorna resultado em tuplas
for item in query.all():
    print(item)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
