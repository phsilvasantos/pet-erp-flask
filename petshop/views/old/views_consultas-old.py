from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_clientes, Form_peludos
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos
from sqlalchemy import desc

views_consultas = Blueprint('views_consultas', __name__)


@views_consultas.route('/')
def index():
    """Index page."""
    listagem = Vendas.query.filter(Vendas.saldo > 0).all()

    if listagem:
        heading = 'Alerta: vendas em aberto'
        tipo = 'vendas'
        return render_template('listagens.html', listagem=listagem, heading=heading, tipo=tipo)

    return render_template('index.html')


@views_consultas.route('/listagem/<tipo>/<int:id>', methods=['GET', 'POST'])
# @views_consultas.route('/listagem/<tipo>', methods=['GET', 'POST'])
def listagens(tipo, id):
    """Listagem de qqer coisa."""
    if tipo == 'vendas':
        listagem = Vendas.query.order_by(desc(Vendas.data_venda)).all()
        heading = 'Últimas vendas'
        return render_template('listagens.html', listagem=listagem, heading=heading, tipo=tipo)

    if tipo == 'clientes':
        listagem = Clientes.query.order_by(Clientes.nome).all()
        heading = 'Relação de clientes'
        return render_template('listagens.html', listagem=listagem, heading=heading, tipo=tipo)

    if tipo == 'peludos':
        # listagem = Peludos.query.order_by(Peludos.nome).all()
        heading = 'Relação de peludos'

        page = request.args.get('page', 1, type=int)
        # blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
        listagem = Peludos.query.order_by(Peludos.nome).paginate(page=page, per_page=8)


        return render_template('listagens.html', listagem=listagem, heading=heading, tipo=tipo)

    if tipo == 'pagamentos':
        venda = Vendas.query.get_or_404(id)
        data = venda.data_venda.strftime('%d-%m-%Y')
        heading = f'Relação de pagamentos para {venda.descricao}, em {data}'
        listagem = Pagamentos.query.filter(Pagamentos.venda_id == venda.id).all()
        return render_template('listagens.html', listagem=listagem, heading=heading, tipo=tipo)


    listagem = Vendas.query.order_by(desc(Vendas.data_venda)).all()
    heading = 'Últimas vendas'
    return render_template('listagens.html', listagem=listagem, heading=heading, tipo=tipo)
