"""Testing crud."""
from pet import db
from pet.models import Cliente, Cachorro, Venda, Contato, Endereco
from datetime import datetime
import pandas as pd

# db.metadata.clear()
# db.create_all()


Cliente.query.all()

aline = Cliente.query.filter_by(nome='Aline').first()
puka = Cachorro.query.filter_by(nome='Puka').first()

sale = Venda(
        descricao='tosa na tesoura', data_venda=datetime(2018, 10, 12),
        valor_venda=100, valor_taxi=10, n_banhos=1, tipo='avulso',
        pacote='---', forma_pagto='cash', data_pagto=datetime(2018,10,12),
        valor_entrada=110
        )

aline.venda.append(sale)






puka.venda.append(sale)

####
comprador = Cliente.query.filter(Cliente.nome.ilike('marcelo')).first()
cao = Cachorro.query.filter(Cachorro.nome.ilike('leon')).first()

sale = Venda(
        descricao='tosa na maquina', data_venda=datetime(2018, 9, 12),
        valor_venda=50, valor_taxi=10, n_banhos=1, tipo='avulso',
        pacote='---', forma_pagto='cash', data_pagto=datetime(2018, 9, 12),
        valor_entrada=60
        )

comprador.venda.append(sale)
cao.venda.append(sale)

db.session.add_all([aline, puka, comprador, cao])
db.session.commit()


# mostra o nome do dono e do Cachorro
query = db.session.query(
    Cliente.nome.label("Cliente"),
    Contato.email.label("mail"),
    Cachorro.nome.label("dog"),
    Cachorro.breed.label('raça'),
    Venda.data_venda.label('data'),
    Venda.valor_entrada.label('valor'),
    Venda.descricao
    ).join(Contato, Cachorro, Venda)


help(db.session.query().join)
# retorna resultado em tuplas
for item in query.all():
    print(item)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
