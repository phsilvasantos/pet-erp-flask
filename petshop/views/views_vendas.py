from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_clientes, Form_peludos, Form_vendas_intro, Form_vendas_bt
from petshop.modelos.models import Clientes, Peludos, Vendas, Pagamentos
from datetime import datetime

views_vendas = Blueprint('views_vendas', __name__)

# tipo = SelectField(u'Tipo de Venda',
#                    choices=[
#                             ('bt', 'Banho&Tosa'),
#                             ('hosp', 'Hospedagem'),
#                             ('curso', 'Cursos'),
#                             ('prod', 'Produtos')
#                             ]
#                    )
@views_vendas.route('/<int:id>', methods=['GET', 'POST'])
def modifica_venda(id):
    """Cadastra vendas."""
    if(id):
        listagem = Vendas.query.get_or_404(id)
        return render_template('lista_vendas.html', listagem=listagem)



@views_vendas.route('/vendas_bt', methods=['GET', 'POST'])
def vendas_bt(id=None):
    """Cadastra vendas."""
    if(id):
        venda = Vendas.query.get_or_404(id)
        return venda

    # se o cliente já foi escolhido,
    # listar os caes e apresentar o form de vendas
    cliente = request.args.get('cliente', None)

    if cliente:
        peludos_cadastrados = Peludos.query.filter(Peludos.cliente_id == cliente).all()
        lista_peludos = [(i.id, i.nome) for i in peludos_cadastrados]

        form = Form_vendas_bt()
        form.peludos.choices = lista_peludos
        nome_cliente = Clientes.query.filter_by(id=cliente).first().nome
        if form.validate_on_submit():
            # peludos = form.peludos.data
            # atribuir ao db
            data_pbanho = form.data_pbanho.data
            data_venda = form.data_venda.data
            descricao = form.descricao.data
            n_banhos = form.n_banhos.data
            pacote = form.pacote.data
            tipo_banho = form.tipo_banho.data
            valor_servicos = form.valor_servicos.data
            valor_taxi = form.valor_taxi.data
            peludo_id = form.peludos.data
            cliente_id = cliente

            # db part
            venda_bt = Vendas(
                            data_pbanho=data_pbanho,
                            data_venda=data_venda,
                            descricao=descricao,
                            n_banhos=n_banhos,
                            pacote=pacote,
                            tipo_banho=tipo_banho,
                            tipo='bt',
                            valor_servicos=valor_servicos,
                            valor_taxi=valor_taxi
                )

            cliente = Clientes.query.get(cliente_id)
            cao = Peludos.query.get(peludo_id)

            cliente.venda.append(venda_bt)
            cao.venda.append(venda_bt)
            db.session.commit()

            return redirect(
                            url_for(
                                    'views_pagamentos.pagamentos',
                                    id=venda_bt.id
                                    )
                            )

        return render_template(
                                'vendas_bt.html',
                                form=form, cliente=cliente,
                                nome_cliente=nome_cliente
                                )

    # senão tiver cliente selecionado, montar lista de clientes que tem cachorro
    # e apresentar form de escolha
    clientes_cadastrados = Clientes.query.filter(Clientes.peludo != None).all()

    lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]
    form = Form_vendas_intro()
    form.cliente.choices = lista_clientes

    if form.validate_on_submit():
        cliente = form.cliente.data
        return redirect(url_for('views_vendas.vendas_bt', cliente=cliente))

    return render_template('vendas_bt.html', form=form)
