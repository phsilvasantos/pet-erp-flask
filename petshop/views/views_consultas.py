from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_clientes, Form_peludos
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos
from sqlalchemy import desc, or_

views_consultas = Blueprint('views_consultas', __name__)


@views_consultas.route('/')
def index():
    """Index page."""
    page = request.args.get('page', 1, type=int)
    # listagem = Vendas.query.filter(
    #     Vendas.saldo > 0).paginate(page=page, per_page=5)
    listagem = (Vendas.query.filter(
        or_(Vendas.saldo > 0, Vendas.saldo == None)
        # ).all())
        ).paginate(page=page, per_page=5))

    if listagem:
        heading = 'Alerta: vendas em aberto'
        tipo = 'vendas'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo)

    return render_template('index.html')


@views_consultas.route('/listagem/<tipo>/<int:id>', methods=['GET', 'POST'])
def listagens(tipo, id):
    """Listagem de qqer coisa."""
    if tipo == 'vendas':
        page = request.args.get('page', 1, type=int)
        listagem = Vendas.query.order_by(
            desc(Vendas.data_venda)).paginate(page=page, per_page=5)
        heading = 'Últimas vendas'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo)

    if tipo == 'clientes':
        page = request.args.get('page', 1, type=int)
        listagem = Clientes.query.order_by(
            Clientes.nome).paginate(page=page, per_page=5)
        heading = 'Relação de clientes'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo)

    if tipo == 'peludos':
        heading = 'Relação de peludos'
        page = request.args.get('page', 1, type=int)
        listagem = Peludos.query.order_by(
            Peludos.nome).paginate(page=page, per_page=5)

        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo)

    if tipo == 'pagamentos':
        venda = Vendas.query.get_or_404(id)
        data = venda.data_venda.strftime('%d-%m-%Y')
        heading = f'Relação de pagamentos para {venda.descricao}, em {data}'
        page = request.args.get('page', 1, type=int)
        listagem = Pagamentos.query.filter(
            Pagamentos.venda_id == venda.id).paginate(page=page, per_page=5)
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo)

    page = request.args.get('page', 1, type=int)
    listagem = Vendas.query.order_by(
        desc(Vendas.data_venda)).paginate(page=page, per_page=5)
    heading = 'Últimas vendas'
    return render_template('listagens.html', listagem=listagem,
                           heading=heading, tipo=tipo)
