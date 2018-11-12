"""Testing crud."""
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos
from datetime import datetime
import pandas as pd

Vendas.query.all()
venda = Vendas.query.first()
venda.saldo()
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
