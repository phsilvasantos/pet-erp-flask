from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_user, logout_user, login_required
from petshop import db
from petshop.modelos.forms import *
from petshop.modelos.models import *

from sqlalchemy import desc, or_

views_consultas = Blueprint('views_consultas', __name__)

@views_consultas.route('/')
def index():
    """Index page."""

    return render_template('index.html')


@views_consultas.route('/landing')
def landing():
    """Index page."""
    page = request.args.get('page', 1, type=int)
    # listagem = Vendas.query.filter(
    #     Vendas.saldo > 0).paginate(page=page, per_page=5)
    # page = 1
    listagem = (Vendas
                .query
                .filter(or_(Vendas.saldo > 0, Vendas.saldo == None))
                .order_by(desc(Vendas.data_venda))
                .paginate(page=page, per_page=5)
                )

    if len(listagem.items):
        heading = 'Alerta: vendas com saldo em aberto'
        tipo = 'aberto'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo, id=0)

    return render_template('login_landing.html')



@views_consultas.route('/listagem/<tipo>/<int:id>', methods=['GET', 'POST'])
def listagens(tipo, id):
    """Listagem de qqer coisa."""
    if tipo == 'aberto':
        page = request.args.get('page', 1, type=int)
        listagem = (Vendas
                    .query
                    .filter(or_(Vendas.saldo > 0, Vendas.saldo == None))
                    .order_by(desc(Vendas.data_venda))
                    .paginate(page=page, per_page=5)
                    )

        heading = 'Alerta: vendas com saldo em aberto'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo, id=0)

    if tipo == 'vendas':
        page = request.args.get('page', 1, type=int)
        listagem = (Vendas.query
                    .order_by(desc(Vendas.data_venda))
                    .paginate(page=page, per_page=5)
                    )
        heading = 'Últimas vendas'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo, id=0)

    if tipo == 'clientes':
        page = request.args.get('page', 1, type=int)
        listagem = Clientes.query.order_by(
            Clientes.nome).paginate(page=page, per_page=5)
        heading = 'Relação de clientes'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo, id=0)

    if tipo == 'peludos':
        heading = 'Relação de peludos'
        page = request.args.get('page', 1, type=int)
        listagem = Peludos.query.order_by(
            Peludos.nome).paginate(page=page, per_page=5)

        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo, id=0)

    if tipo in ['pagamentos', 'd_pagamentos']:
        # page = 1
        venda = Vendas.query.get_or_404(id)
        tem_pagamentos = len(venda.pagamentos)
        data = venda.data_venda.strftime('%d-%m-%Y')
        total = venda.calcula_saldo('total')
        heading = [f'Relação de pagamentos para {venda.descricao}, de {data}',
                   f'Valor total: R${total}',
                   f'Saldo: R${venda.saldo}']
        page = request.args.get('page', 1, type=int)
        listagem = (Pagamentos.query.filter(
                                            Pagamentos.venda_id == venda.id)
                                            .paginate(page=page, per_page=5)
                    )

        return render_template('listagens.html', listagem=listagem,
                               saldo=venda.saldo,
                               heading=heading, tipo=tipo, id=0,
                               tem_pagamentos=tem_pagamentos)

    if tipo == 'ver_vendas':
        cliente = Clientes.query.get(id)
        heading = f'Últimas vendas para {cliente.nome}'

        page = request.args.get('page', 1, type=int)
        listagem = (Vendas.query
                    .filter(Vendas.cliente_id == id)
                    .order_by(desc(Vendas.data_venda))
                    .paginate(page=page, per_page=5)
                    )
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo, id=id)

    return redirect(url_for('views_consultas.index'))


@views_consultas.route('/details/<tipo>/<int:id>', methods=['GET', 'POST'])
def details(tipo, id):
    """Detalhamento de qqer coisa."""
    if tipo in ['aberto', 'vendas', 'ver_vendas']:
        venda = Vendas.query.get(id)
        data = venda.data_venda.strftime('%d-%m-%Y')
        total = venda.calcula_saldo('total')
        saldo = venda.saldo
        cliente = Clientes.query.get(venda.cliente_id)
        tem_pagamentos = len(venda.pagamentos)
        # saldo = venda.saldo
        heading = [f'Detalhes para {venda.descricao}',
                   f'Descrição: {venda.descricao}',
                   f'Cliente: {cliente.nome}',
                   f'Data da venda: {data}',
                   f'Valor total: {total}',
                   f'Saldo: {venda.saldo}'
                   ]

        return render_template('details.html', item=venda,
                               heading=heading, tipo=tipo,
                               saldo=saldo,
                               tem_pagamentos=tem_pagamentos)

    if tipo == 'clientes':
        # cliente = Clientes.query.first()

        cliente = Clientes.query.get(id)
        endereco = Enderecos.query.filter(Enderecos.cliente_id == cliente.id).first()
        contato = Contatos.query.filter(Contatos.cliente_id == cliente.id).first()
        peludos = Peludos.query.filter(Peludos.cliente_id == cliente.id).all()
        peludos = [pel.nome for pel in peludos]
        peludos = ' | '.join(peludos)
        vendas = Vendas.query.filter(Vendas.cliente_id == cliente.id).all()

        heading = [f'Detalhes para {cliente.nome}',
                   f'Contato: {contato}',
                   f'Endereço: {endereco}',
                   f'Responsável por {peludos}']

        return render_template('details.html', item=cliente,
                               heading=heading, tipo=tipo, vendas=vendas)

    if tipo == 'peludos':
        peludo = Peludos.query.get(id)
        cliente = Clientes.query.get(peludo.cliente_id)
        heading = [f'Detalhes para {peludo.nome}',
                   f'Dono: {cliente.nome}',
                   f'Raça: {peludo.breed}',
                   f'Idade: {peludo.get_idade()}, sexo: {peludo.sexo}'
                   ]

        return render_template('details.html', item=peludo,
                               heading=heading, tipo=tipo)

    if tipo in ['d_pagamento', 'pagamentos']:
        pagamento = Pagamentos.query.get(id)
        venda = Vendas.query.get(pagamento.venda_id)
        data = venda.data_venda.strftime('%d-%m-%Y')
        total = venda.calcula_saldo('total')
        heading = [f'Detalhes para pagamento de {pagamento.valor}',
                   f'Referente a {venda.descricao}, de {data}',
                   f'Forma de pagamento: {pagamento.forma_pagto}',
                   f'Valor total da venda: R${total}',
                   f'Saldo da venda: R${venda.saldo}']

        return render_template('details.html', item=pagamento,
                               heading=heading, tipo=tipo)

    return redirect(url_for('views_consultas.index'))
