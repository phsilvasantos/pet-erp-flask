from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_clientes, Form_peludos
from petshop.modelos.models import Clientes, Peludos, Contatos, Enderecos, Vendas

views_consultas = Blueprint('views_consultas', __name__)


@views_consultas.route('/')
def index():
    """Index page."""

    ########
    venda_comsaldo = Vendas.query.filter(Vendas.saldo != 0).all()

    # for item in venda_comsaldo:
    #     print(item.saldo(), item.descricao)


    return render_template('index.html', venda_comsaldo=venda_comsaldo)



@views_consultas.route('/lista_clientes')
def lista_clientes():
    # page = request.args.get('page', 1, type=int)
    # listagem = Cliente.query.order_by(Cliente.nome).paginate(page=page, per_page=10)
    # listagem = ['teste']
    listagem = Clientes.query.all()
    return render_template('lista_clientes.html', listagem=listagem)
