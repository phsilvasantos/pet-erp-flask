"""Testing crud."""
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos, Contatos
from datetime import datetime
import pandas as pd

# db.metadata.clear()
# db.create_all()


Clientes.query.all()

aline = Clientes.query.filter_by(nome='Aline').first()
puka = Peludos.query.filter_by(nome='Puka').first()

aline

puka

sale = Vendas(
        descricao='tosa na tesoura', data_venda=datetime(2018, 10, 12),
        data_pbanho=datetime(2018, 11, 5), valor_servicos=300, valor_taxi=10,
        n_banhos=5, tipo='pacote', pacote='puka'
        )



aline.venda.append(sale)


puka.venda.append(sale)

####
comprador = Clientes.query.filter(Clientes.nome.ilike('marcelo')).first()
cao = Peludos.query.filter(Peludos.nome.ilike('leon')).first()

sale = Vendas(
        descricao='tosa na maquina', data_venda=datetime(2018, 11, 5),
        data_pbanho=datetime(2018, 11, 5), valor_servicos=200, valor_taxi=20,
        n_banhos=4, tipo='pacote', pacote='puka'
        )

comprador.venda.append(sale)
cao.venda.append(sale)

# db.session.add_all([aline, puka, comprador, cao])
db.session.commit()

# mostra o nome do dono e do Peludo
query = db.session.query(
    Clientes.nome.label("Cliente"),
    Contatos.email.label("mail"),
    Peludos.nome.label("dog"),
    Peludos.breed.label('raça'),
    Vendas.data_venda.label('data'),
    Vendas.valor_servicos.label('valor'),
    Vendas.descricao
    ).join(Contatos, Peludos, Vendas)


# retorna resultado em tuplas
for item in query.all():
    print(item)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df

##########
Vendas.query.all()
### Cadastro Pagamentos
venda = Vendas.query.filter_by(valor_servicos=501).first()

venda
venda.valor_taxi
