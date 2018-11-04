"""Testing crud."""
from petshop import db
from petshop.models import Clientes, Peludos, Vendas_bt, Pagamentos
from datetime import datetime
import pandas as pd

venda = Vendas_bt(
                descricao = 'uma venda', data_venda = datetime(2018, 11, 1),
                data_pbanho = datetime(2018, 12, 1),
                valor_servicos = 100, valor_taxi = 10, n_banhos = 2,
                tipo_banho = 'avulso', pacote = 'puka'
                )

cliente = Clientes.query.filter_by(nome='Marcelo').first()
cliente

cao = Peludos.query.filter_by(nome='Leon').first()
cao


cliente.venda_bt.append(venda)
cao.venda_bt.append(venda)

db.session.commit()
# db.session.rollback()

##
Vendas_bt.query.all()

########
pagamento = Pagamentos(data = datetime(2018, 11, 4), valor = 25,
                        forma_pagto = 'credito', valor_entrada = 23)


venda = Vendas_bt.query.first()
venda
venda.pagamentos.append(pagamento)
db.session.commit()

#### 2nd parcela
pagamento = Pagamentos(data = datetime(2018, 11, 3), valor = 55,
                        forma_pagto = 'credito', valor_entrada = 53)


venda = Vendas_bt.query.first()
venda
venda.pagamentos.append(pagamento)
db.session.commit()


Pagamentos.query.all()


# mostra o nome do dono e do peludo
query = db.session.query(
                            Clientes.nome.label("Cliente"),
                            Peludos.nome.label("dog"),
                            Vendas_bt.descricao,
                            Vendas_bt.valor_servicos,
                            Pagamentos.data,
                            Pagamentos.valor,
                            Pagamentos.forma_pagto
                        ).join(Peludos, Vendas_bt, Pagamentos)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
