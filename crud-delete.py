"""Testing crud."""
from petshop import db
from petshop.models import Clientes, Peludos, Contatos, Enderecos, Vendas, Pagamentos



Clientes.query.delete()
Peludos.query.delete()
Contatos.query.delete()
Enderecos.query.delete()
Vendas.query.delete()
db.session.commit()
# db.session.rollback()

## read Cliente
Clientes.query.all()
