"""Testing crud."""
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos
from datetime import datetime
import pandas as pd

venda_bt = Vendas(
                data_pbanho=datetime(2018, 11, 1),
                data_venda=datetime(2018, 11, 1),
                descricao='barba e bigode',
                n_banhos=5,
                pacote='puka',
                tipo_banho='pacote',
                tipo='bt',
                valor_servicos=200,
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
pagamento = Pagamentos(data = datetime(2018, 11, 4), valor = 25,
                        forma_pagto = 'credito', valor_entrada = 23)


venda = Vendas.query.first()
venda
venda.pagamentos.append(pagamento)
db.session.commit()

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
