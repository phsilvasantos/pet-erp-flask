from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_pagamentos
from petshop.modelos.models import Vendas, Pagamentos
from datetime import datetime

views_pagamentos = Blueprint('views_pagamentos', __name__)

# tipo = SelectField(u'Tipo de Venda',
#                    choices=[
#                             ('bt', 'Banho&Tosa'),
#                             ('hosp', 'Hospedagem'),
#                             ('curso', 'Cursos'),
#                             ('prod', 'Produtos')
#                             ]
#                    )


@views_pagamentos.route('/pagamentos/<int:id>', methods=['GET', 'POST'])
def pagamentos(id):
    """Cadastra pagamentos."""
    if id:
        venda = Vendas.query.filter_by(id=id).first()
    else:
        venda = request.args.get('id', None)
        venda = Vendas.query.filter_by(id=id).first()

    descricao = venda.descricao
    saldo = venda.calcula_saldo()
    form = Form_pagamentos()

    if form.validate_on_submit():
        data = form.data.data
        forma_pagto = form.forma_pagto.data
        valor = form.valor.data
        valor_entrada = form.valor_entrada.data

        # db parts
        pagamento = Pagamentos(
                                data=data,
                                forma_pagto=forma_pagto,
                                valor=valor,
                                valor_entrada=valor_entrada
                                )

        # db.session.add(venda_bt)
        venda.pagamentos.append(pagamento)
        venda.saldo = venda.calcula_saldo()
        db.session.commit()

        return redirect(url_for('views_consultas.index'))

    return render_template(
                            'pagamentos.html',
                            form=form, venda=venda, descricao=descricao, saldo=saldo
                            )
