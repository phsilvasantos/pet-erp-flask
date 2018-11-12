"""Testing crud."""
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Vendas, Contatos, Enderecos
from datetime import datetime
import pandas as pd

# db.metadata.clear()
# db.create_all()


Clientes.query.all()

cliente = Clientes.query.filter_by(nome='Aline').first()
cliente


# seletor para forms - clientes
db.session.query(Clientes).all()
clientes_cadastrados = db.session.query(Clientes).all()
lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]
lista_clientes

#seletor de caes para um cliente
peludos_cadastrados = db.session.query(Peludos).filter(Peludos.cliente_id == 1).all()
lista_peludos = [(i.id, i.nome) for i in peludos_cadastrados]
lista_peludos


# nome atraves de id
sel = db.session.query(Clientes).filter(Clientes.id == 1).first()
sel.nome
Clientes.query.filter_by(id=1).first().nome

query = db.session.query(
    Cliente.nome.label("Cliente"),
    Contato.email.label("mail"),
    Peludo.nome.label("dog"),
    Peludo.breed.label('raça'),
    Venda.data_venda.label('data'),
    Venda.valor_entrada.label('valor'),
    Venda.descricao
    ).join(Contato, Peludo, Venda)


help(db.session.query().join)
# retorna resultado em tuplas
for item in query.all():
    print(item)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
