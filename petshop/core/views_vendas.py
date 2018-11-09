from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.forms import Form_clientes, Form_peludos, Form_vendas_intro, Form_vendas_bt
from petshop.models import Clientes, Peludos, Contatos, Enderecos

views_vendas = Blueprint('views_vendas', __name__)

# tipo = SelectField(u'Tipo de Venda',
#                    choices=[
#                             ('bt', 'Banho&Tosa'),
#                             ('hosp', 'Hospedagem'),
#                             ('curso', 'Cursos'),
#                             ('prod', 'Produtos')
#                             ]
#                    )


@views_vendas.route('/vendas_bt', methods=['GET', 'POST'])
def vendas_bt():
    """Cadastra vendas."""
    cliente = request.args.get('cliente', None)

    # se o cliente já foi escolhido, listar os caes e apresentar o form de vendas
    if cliente:
        peludos_cadastrados = Peludos.query.filter(Peludos.cliente_id == cliente).all()
        lista_peludos = [(i.id, i.nome) for i in peludos_cadastrados]

        form = Form_vendas_bt()
        form.peludos.choices = lista_peludos
        nome_cliente = Clientes.query.filter_by(id=cliente).first().nome
        if form.validate_on_submit():
            # peludos = form.peludos.data
            # atribuir ao db
            return redirect(url_for('views_consultas.index'))

        return render_template(
                                'vendas_bt.html',
                                form=form, cliente=cliente,
                                nome_cliente=nome_cliente
                                )

    # senão tiver cliente selecionado, montar lista de clientes e apresentar form de escolha
    clientes_cadastrados = db.session.query(Clientes).all()
    lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]
    form = Form_vendas_intro()
    form.cliente.choices = lista_clientes

    if form.validate_on_submit():
        cliente = form.cliente.data
        return redirect(url_for('views_vendas.vendas_bt', cliente=cliente))

    return render_template('vendas_bt.html', form=form)
