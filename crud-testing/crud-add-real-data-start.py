"""Testing crud."""
from petshop import db
from petshop.modelos.models import *
from datetime import datetime
import pandas as pd
from sqlalchemy import or_, and_

import sqlite3 #To write database

del df
df = pd.read_excel('cadastro_sistema.xlsx')
df = df.dropna(subset=['CPF'])
df.CPF = df.CPF.apply(str)
df.CPF = df.CPF.str.split('.').str[0]

# clientes
df_clientes = df.iloc[:,:14].copy()

colunas = ['id', 'nascimento', 'profissao', 'nome', 'tel1', 'tel2',
           'email', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'cep', 'distancia']

df_clientes.columns = colunas


df_pessoas = df_clientes.copy()
df_pessoas = df_pessoas.iloc[:,:4]
df_pessoas['sexo'] = 'M'
df_pessoas.columns
df_pessoas = df_pessoas[~df_pessoas.duplicated()]
df_pessoas.shape



cxn = sqlite3.connect('petshop/data.sqlite')
df_pessoas.to_sql('clientes', cxn, index=False, if_exists='append')

query = db.session.query(
    Clientes.nome,
    Clientes.id,
    Clientes.nascimento,
    Clientes.profissao
    )

df = pd.read_sql(query.statement, db.session.bind)
df

# endereços

for item in enumerate(df_clientes.columns):
    print(item)

df_enderecos = df_clientes.iloc[:,[0,7,8,9,10,11,12,13]].copy()
df_enderecos.columns
df_enderecos['estado'] = 'SP'

df_enderecos = df_enderecos.rename({'id': 'cliente_id'}, axis=1)
df_enderecos['id'] = df_enderecos.index + 2

df_enderecos.cep = df_enderecos.cep.apply(str).str.split('.').str[0]
df_enderecos.cep = str(0) + df_enderecos.cep

df_enderecos.head()
cxn = sqlite3.connect('petshop/data.sqlite')
df_enderecos.to_sql('enderecos', cxn, index=False, if_exists='append')

# testing
enderecos = Enderecos.query.all()
endereco = enderecos[0]
endereco.rua
endereco.cep
endereco.distancia


# contatos
for item in enumerate(df_clientes.columns):
    print(item)
df_ingesting = df_clientes.iloc[:,[0,4,5,6]].copy()

df_ingesting = df_ingesting.rename({'id': 'cliente_id'}, axis=1)
df_ingesting['id'] = df_enderecos.index + 2
df_ingesting.head()

df_ingesting.to_sql('contatos', cxn, index=False, if_exists='append')

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

#######

for item in enumerate(df.columns):
    print(item)

df_ingesting = df.iloc[:, [0, 16, 17, 18, 19, 20, 21, 22]].copy()

df_ingesting.columns

df_ingesting.columns = ['cliente_id', 'nome', 'breed',
                        'sexo', 'pelagem', 'nascimento', 'data_start', 'castrado']

df_ingesting['id'] = df_enderecos.index + 2

df_ingesting.head()
df_ingesting.to_sql('peludos', cxn, index=False, if_exists='append')

# testing
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
clientes = Clientes.query.all()
aline = clientes[0]
aline

aline.id
aline.nome
aline.nascimento
aline.profissao
aline.endereco
aline.contato

for cliente in clientes:
    print(cliente)

endereco = Enderecos.query.first()
endereco.cliente_id
endereco.id


contato = Contatos.query.first()
contato

contato.id
contato.cliente_id
contato.tel1
contato.tel2
####

id = "31554651824"
erick = Clientes.query.get(id)
erick
erick.id
erick.nome
erick.endereco
erick.nascimento
erick.contato

endereco = Enderecos.query.filter(Enderecos.cliente_id == id).all()
endereco

Enderecos.query.all()

Peludos.query.filter(Peludos.cliente_id == '31554651824').all()
Peludos.query.all()
