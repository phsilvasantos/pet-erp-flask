"""Testing crud."""
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos
from datetime import datetime
import pandas as pd

venda_bt = Vendas(
                data_pbanho=datetime(2018, 11, 15),
                data_venda=datetime(2018, 11, 15),
                descricao='barba e bigode 2',
                n_banhos=8,
                pacote='puka',
                tipo_banho='pacote',
                tipo='bt',
                valor_servicos=1200,
                valor_taxi=0,
    )

cliente = Clientes.query.filter_by(nome='Marcelo').first()
cliente

cao = Peludos.query.filter_by(nome='Leon').first()
cao


cliente.venda.append(venda_bt)
cao.venda.append(venda_bt)

db.session.commit()
# db.session.rollback()

##
Vendas.query.all()

########
pagamento = Pagamentos(data = datetime(2018, 11, 15), valor = 222,
                        forma_pagto = 'credito', valor_entrada = 222)


venda = Vendas.query.get(3)
venda
venda.saldo
venda.pagamentos.append(pagamento)

venda.saldo = venda.calcula_saldo()

db.session.commit()

Vendas.query.filter(Vendas.saldo > 0).all()


#### 2nd parcela
pagamento = Pagamentos(data = datetime(2018, 11, 3), valor = 55,
                        forma_pagto = 'credito', valor_entrada = 53)


venda = Vendas.query.first()
venda
venda.pagamentos.append(pagamento)
db.session.commit()


Pagamentos.query.all()


# mostra o nome do dono e do peludo
query = (
        db.session.query(
                            Clientes.nome.label("Cliente"),
                            Peludos.nome.label("dog"),
                            Vendas.descricao,
                            Vendas.valor_servicos,
                            Pagamentos.data,
                            Pagamentos.valor,
                            Pagamentos.forma_pagto
                        )
        .join(Peludos, Vendas, Pagamentos)
        )


# listando os pagamentos para uma venda
venda = Vendas.query.first()
venda

venda.pagamentos
venda.saldo()



# coloca em df



df = pd.read_sql(query.statement, db.session.bind)
df
