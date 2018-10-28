from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.forms import Form_clientes, Form_peludos, Form_vendas_intro, Form_vendas
from petshop.models import Clientes, Peludos, Vendas, Contatos, Enderecos
# from wtforms.ext.sqlalchemy.orm import model_form
# from wtforms_alchemy import ModelForm


core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('index.html')


@core.route('/cadastro_clientes', methods=['GET', 'POST'])
def cadastro_clientes():
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

        #db part
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


@core.route('/cadastro_peludos', methods=['GET', 'POST'])
def cadastro_peludos():

    clientes_cadastrados = db.session.query(Clientes).all()
    lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]

    form = Form_peludos()
    form.cliente.choices = lista_clientes

    if form.validate_on_submit():
        cliente = form.cliente.data
        nome = form.nome.data
        sexo = form.sexo.data
        breed = form.breed.data
        pelagem = form.pelagem.data
        nascimento = form.nascimento.data.strftime('%d-%m-%Y')
        data_start = form.data_start.data.strftime('%d-%m-%Y')
        castrado = form.castrado.data
        return redirect(url_for('core.lista_clientes'))

    return render_template('cadastro_peludos.html', form=form)


@core.route('/cadastro_vendas', methods=['GET', 'POST'])
def cadastro_vendas():

    cliente = request.args.get('cliente', None)

    # se o cliente já foi escolhido, listar os caes e apresentar o form de vendas
    if cliente:
        peludos_cadastrados = db.session.query(Peludos).filter(Peludos.cliente_id == cliente).all()
        lista_peludos = [(i.id, i.nome) for i in peludos_cadastrados]

        form = Form_vendas()
        form.peludos.choices = lista_peludos
        nome_cliente = Clientes.query.filter_by(id=cliente).first().nome
        if form.validate_on_submit():
            peludos = form.peludos.data
            return redirect(url_for('core.index'))

        return render_template(
                                'cadastro_vendas.html',
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
        return redirect(url_for('core.cadastro_vendas', cliente=cliente))

    return render_template('cadastro_vendas.html', form=form)



@core.route('/lista_clientes')
def lista_clientes():
    # page = request.args.get('page', 1, type=int)
    # listagem = Cliente.query.order_by(Cliente.nome).paginate(page=page, per_page=10)
    # listagem = ['teste']
    listagem = Clientes.query.all()
    return render_template('lista_clientes.html', listagem=listagem)
