from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.forms import Form_clientes, Form_peludos, Form_vendas_intro, Form_vendas
from petshop.models import Clientes, Peludos, Contatos, Enderecos

views_cadastros = Blueprint('views_cadastros', __name__)


@views_cadastros.route('/cadastro_clientes', methods=['GET', 'POST'])
def cadastro_clientes():
    """Cadastra clientes."""
    form = Form_clientes()

    if form.validate_on_submit():
        nome = form.nome.data
        sexo = form.sexo.data
        tel1 = form.tel1.data
        tel2 = form.tel2.data
        email = form.email.data
        rua = form.rua.data
        numero = form.numero.data
        bairro = form.bairro.data
        cidade = form.cidade.data
        estado = form.estado.data
        distancia = form.distancia.data

        # db part
        n_cliente = Clientes(nome=nome, sexo=sexo)
        n_endereco = Enderecos(rua=rua, numero=numero, bairro=bairro, cidade=cidade,
                               estado=estado, distancia=distancia)

        n_contato = Contatos(tel1=tel1, tel2=tel2, email=email)

        n_cliente.endereco.append(n_endereco)
        n_cliente.contato.append(n_contato)
        db.session.add(n_cliente)
        db.session.commit()

        return redirect(url_for('core.lista_clientes'))

    return render_template('cadastro_clientes.html', form=form)


@views_cadastros.route('/cadastro_peludos', methods=['GET', 'POST'])
def cadastro_peludos():
    """Cadastra peludos."""
    clientes_cadastrados = Clientes.query.all()
    lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]

    form = Form_peludos()
    form.cliente.choices = lista_clientes

    if form.validate_on_submit():
        cliente = form.cliente.data
        nome = form.nome.data
        sexo = form.sexo.data
        breed = form.breed.data
        pelagem = form.pelagem.data
        nascimento = form.nascimento.data
        data_start = form.data_start.data
        castrado = form.castrado.data

        # db part
        n_peludo = Peludos(nome, breed, pelagem, nascimento,
                           data_start, sexo, castrado)

        n_cliente = Clientes.query.get(cliente)

        db.session.add(n_peludo)
        n_cliente.peludo.append(n_peludo)
        db.session.commit()

        return redirect(url_for('core.lista_clientes'))

    return render_template('cadastro_peludos.html', form=form)
