from datetime import datetime
from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_required
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Vendas
from petshop.modelos.forms import (
                        Form_vendas_intro, Form_vendas_bt,
                        Form_vendas_hosp, Form_vendas_cursos, Form_vendas_prod
                        )

views_vendas = Blueprint('views_vendas', __name__)


@views_vendas.route('/<int:id>', methods=['GET', 'POST'])
@login_required
def modifica_venda(id):
    """Cadastra vendas."""
    if(id):
        listagem = Vendas.query.get_or_404(id)
        return render_template('lista_vendas.html', listagem=listagem)


@views_vendas.route('/vendas/<tipo>', methods=['GET', 'POST'])
@login_required
def vendas(tipo):
    """Cadastra vendas."""
    # se o cliente já foi escolhido,
    # listar os caes e apresentar o form de vendas
    tipo_dic = {'bt': 'Banho & Tosa',
                'hosp': 'Hospedagem',
                'cursos': 'Cursos',
                'produtos': 'Produtos'
                }

    cliente_id = request.args.get('cliente_id', None)

    if cliente_id:
        cliente = Clientes.query.get(cliente_id)
        peludos_cadastrados = Peludos.query.filter(Peludos.cliente_id == cliente_id).all()
        lista_peludos = [(i.id, i.nome) for i in peludos_cadastrados]
        lista_peludos = sorted(lista_peludos, key=lambda item: item[1])

        # vendas bt
        if tipo == 'bt':
            form = Form_vendas_bt()
            form.peludos.choices = lista_peludos
            if form.validate_on_submit():
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

                # db part
                venda_n = Vendas(
                                data_pbanho=data_pbanho,
                                data_venda=data_venda,
                                descricao=descricao,
                                n_banhos=n_banhos,
                                pacote=pacote,
                                tipo_banho=tipo_banho,
                                tipo=tipo,
                                valor_servicos=valor_servicos,
                                valor_taxi=valor_taxi
                    )

                peludos = Peludos.query.filter(Peludos.id.in_(peludo_id)).all()
                for cao in peludos:
                    cao.vendas_on_peludo.append(venda_n)

                cliente.venda.append(venda_n)
                db.session.commit()

                return redirect(
                                url_for(
                                        'views_pagamentos.pagamentos',
                                        id=venda_n.id
                                        )
                                )

            return render_template(
                                    'vendas.html',
                                    form=form, cliente=cliente_id,
                                    nome_cliente=cliente.nome,
                                    tipo=tipo
                                    )

        # vendas hospedagem
        if tipo == 'hosp':
            form = Form_vendas_hosp()
            form.peludos.choices = lista_peludos
            if form.validate_on_submit():
                # atribuir ao db
                data_entrada = form.data_entrada.data
                data_saida = form.data_saida.data
                data_venda = form.data_venda.data
                descricao = form.descricao.data
                n_banhos = form.n_banhos.data
                valor_diarias = form.valor_diarias.data
                valor_servicos = form.valor_servicos.data
                valor_taxi = form.valor_taxi.data
                peludo_id = form.peludos.data

                # db part
                venda_n = Vendas(
                            data_entrada=data_entrada,
                            data_saida=data_saida,
                            data_venda=data_venda,
                            descricao=descricao,
                            n_banhos=n_banhos,
                            valor_diarias=valor_diarias,
                            valor_servicos=valor_servicos,
                            valor_taxi=valor_taxi,
                            tipo=tipo
                    )

                peludos = Peludos.query.filter(Peludos.id.in_(peludo_id)).all()
                for cao in peludos:
                    cao.vendas_on_peludo.append(venda_n)

                cliente.venda.append(venda_n)
                db.session.commit()

                return redirect(
                                url_for(
                                        'views_pagamentos.pagamentos',
                                        id=venda_n.id
                                        )
                                )

            return render_template(
                                    'vendas.html',
                                    form=form, cliente=cliente_id,
                                    nome_cliente=cliente.nome,
                                    tipo=tipo
                                    )

        if tipo == 'cursos':
            form = Form_vendas_cursos()
            if form.validate_on_submit():
                # atribuir ao db
                data_entrada = form.data_entrada.data
                data_saida = form.data_saida.data
                data_venda = form.data_venda.data
                descricao = form.descricao.data
                valor_servicos = form.valor_servicos.data
                custo_prod = form.custo_prod.data

                # db part
                venda_n = Vendas(
                            data_entrada=data_entrada,
                            data_saida=data_saida,
                            data_venda=data_venda,
                            descricao=descricao,
                            valor_servicos=valor_servicos,
                            custo_prod=custo_prod,
                            tipo=tipo
                    )

                cliente.venda.append(venda_n)
                db.session.commit()

                return redirect(
                                url_for(
                                        'views_pagamentos.pagamentos',
                                        id=venda_n.id
                                        )
                                )

            return render_template(
                                    'vendas.html',
                                    form=form, cliente=cliente_id,
                                    nome_cliente=cliente.nome,
                                    tipo=tipo
                                    )

        if tipo == 'produtos':
            form = Form_vendas_prod()
            if form.validate_on_submit():
                # atribuir ao db
                data_venda = form.data_venda.data
                descricao = form.descricao.data
                valor_prod = form.valor_prod.data
                custo_prod = form.custo_prod.data
                quantidade = form.quantidade.data

                # db part
                venda_n = Vendas(
                            data_venda=data_venda,
                            descricao=descricao,
                            valor_prod=valor_prod,
                            custo_prod=custo_prod,
                            quantidade=quantidade,
                            tipo=tipo
                    )

                cliente.venda.append(venda_n)
                db.session.commit()

                return redirect(
                                url_for(
                                        'views_pagamentos.pagamentos',
                                        id=venda_n.id
                                        )
                                )

            return render_template(
                                    'vendas.html',
                                    form=form, cliente=cliente_id,
                                    nome_cliente=cliente.nome,
                                    tipo=tipo
                                    )
    # senão tiver cliente selecionado, montar lista de clientes que tem cachorro
    # e apresentar form de escolha
    else:
        clientes_cadastrados = Clientes.query.filter(Clientes.peludo != None).all()
        lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]
        lista_clientes = sorted(lista_clientes, key=lambda item: item[1])

        form = Form_vendas_intro()
        form.cliente.choices = lista_clientes

        if form.validate_on_submit():
            cliente_id = form.cliente.data
            return redirect(
                url_for('views_vendas.vendas',
                        tipo=tipo, cliente_id=cliente_id,
                        )
                    )

        return render_template('vendas.html', form=form, tipo_dic=tipo_dic[tipo])
