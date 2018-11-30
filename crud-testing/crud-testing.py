"""Testing crud."""
from petshop import db
from petshop.modelos.models import *
from datetime import datetime
import pandas as pd
from sqlalchemy import or_, and_

import sqlite3 #To write database


cap = Clientes.query.get(666)
cap.endereco

teste = Clientes.query.first()
teste.endereco[0]
teste


query = db.session.query(
    Clientes.nome,
    Clientes.id,
    Clientes.nascimento,
    Clientes.profissao

    )

df = pd.read_sql(query.statement, db.session.bind)
df

clientes = Clientes.query.all()

# testing
contatos = Contatos.query.all()
contato = contatos[0]
contato
contato.email
contato.id

#
query = db.session.query(
    Clientes.nome,
    Clientes.id,
    Enderecos.rua,
    Enderecos.bairro,
    Contatos.email).join(Enderecos, Contatos)

df_testing = pd.read_sql(query.statement, db.session.bind)
df_testing

# caes


caes = Peludos.query.all()
cao = caes[0]
cao
cao.nome

query = db.session.query(
    Clientes.nome.label('cliente'),
    Clientes.id,
    Enderecos.rua,
    Enderecos.bairro,
    Contatos.email,
    Peludos.nome,
    Peludos.breed,
    Peludos.nascimento
    ).join(Enderecos, Contatos, Peludos)

df_testing = pd.read_sql(query.statement, db.session.bind)
df_testing.to_excel('testing.xlsx', index=False)
df_testing

#
