"""Testing crud."""
from petshop import db
from petshop.models import *

from datetime import datetime
import pandas as pd



# db.session.rollback()

## read Cliente

Clientes.query.all()
Peludos.query.all()

teste = Clientes.query.get(1)
teste
Clientes.query.filter_by(nome='Aline').first()


# query = db.session.query(Cliente).order_by(Cliente.id)
# for _row in query.all():
#     print(_row.nome, _row.id)

## create peludo

def get_id(termo):
    # query = db.session.query(Cliente).filter_by(nome=nome).all()
    dono = db.session.query(Cliente).filter(Cliente.nome.ilike(termo)).first()
    return dono.id

get_id('aline')




# db.session.add(new)
# db.session.commit()
# db.session.rollback()
# peludo.query.all()
# peludo.query.get(1)
# peludo.query.filter(peludo.nome.ilike('puka')).first()
Clientes.query.all()

clientes_cadastrados = Clientes.query.all()
lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]
lista_clientes

caes_aline = Clientes.query.filter_by(nome='Aline').first().peludo
caes_aline
caes_aline = [(i.id, i.nome, i.cliente_id) for i in caes_aline]



Peludos.query.all()


### testando backref
teste = Peludos.query.filter_by(nome='Puka').first()
teste.cliente_id
teste.clientes

######
cliente = Clientes.query.filter_by(nome='Marcelo').first()

Peludos.query.filter(Peludos.cliente_id == cliente.id).all()


peludos_cadastrados = db.session.query(Peludos).filter(Peludos.cliente_id == cliente.id).all()
peludos_cadastrados = Peludos.query.filter(Peludos.cliente_id == cliente.id).all()
lista_peludos = [(i.id, i.nome) for i in peludos_cadastrados]
lista_peludos
