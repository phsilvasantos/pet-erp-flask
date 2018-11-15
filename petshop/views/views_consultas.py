from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_clientes, Form_peludos
from petshop.modelos.models import Clientes, Peludos, Contatos, Enderecos, Vendas
from sqlalchemy import desc

views_consultas = Blueprint('views_consultas', __name__)


@views_consultas.route('/')
def index():
    """Index page."""
    listagem = Vendas.query.filter(Vendas.saldo > 0).all()

    if listagem:
        heading = 'Alerta: vendas em aberto'
        return render_template('listagens.html', listagem=listagem, heading=heading)

    return render_template('index.html')


@views_consultas.route('/listagem/<tipo>')
def listagens(tipo='bt'):
    """Listagem de qqer bosta."""
    if tipo == 'bt':
        listagem = Vendas.query.order_by(desc(Vendas.data_venda)).all()
        heading = 'Últimas vendas de BT'
        return render_template('listagens.html', listagem=listagem, heading=heading)

    listagem = Vendas.query.order_by(desc(Vendas.data_venda)).all()
    heading = 'Últimas vendas'
    return render_template('listagens.html', listagem=listagem, heading=heading)
