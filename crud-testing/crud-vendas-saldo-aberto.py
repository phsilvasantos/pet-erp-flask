"""Testing crud."""
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos
from datetime import datetime
import pandas as pd
from sqlalchemy import or_, and_

Vendas.query.all()

len(Vendas.query.all())

vendas = Vendas.query.filter(Vendas.tipo=='hosp').all()
vendas

listagem = (Vendas
            .query.filter(
                        and_(
                            or_(Vendas.saldo > 0, Vendas.saldo == None ),
                            Vendas.tipo == 'hosp'
                            )
                        ).all()
            )
listagem




########
venda_comsaldo = Vendas.query.filter(Vendas.saldo != 0).all()
venda_comsaldo

for item in venda_comsaldo:
    print(item.saldo(), item.descricao)

Pagamentos.query.all()


# mostra o nome do dono e do peludo
query = (
        db.session.query(
                            Clientes.nome,
                            Vendas.descricao,
                            Vendas.valor_servicos,
                        )
        .join(Vendas, Pagamentos)
        .filter(Vendas.saldo != 0)
        )


df = pd.read_sql(query.statement, db.session.bind)
df
