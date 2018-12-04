"""Testing crud."""
from petshop import db
from petshop.modelos.models import *



Clientes.query.delete()
Peludos.query.delete()
Contatos.query.delete()
Enderecos.query.delete()
Vendas.query.delete()
Pagamentos.query.delete()
db.session.commit()
db.session.rollback()

## read Cliente
Clientes.query.all()
