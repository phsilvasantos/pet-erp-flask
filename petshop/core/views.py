from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.forms import Form_cliente
from petshop.models import Cliente, Cachorro, Venda, Contato, Endereco


core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('index.html')


@core.route('/cadastro_caes')
def lista_clientes():
    # page = request.args.get('page', 1, type=int)
    # listagem = Cliente.query.order_by(Cliente.nome).paginate(page=page, per_page=10)
    # listagem = ['teste']
    listagem = Cliente.query.all()
    return render_template('lista_donos.html', listagem=listagem)


@core.route('/cadastro_clientes', methods=['GET', 'POST'])
def cadastro_clientes():
    form = Form_cliente()

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
        n_cliente = Cliente(nome=nome, sexo=sexo)
        n_endereco = Endereco(rua=rua, numero=numero, bairro=bairro, cidade=cidade,
            estado=estado, distancia=distancia)

        n_contato = Contato(tel1=tel1, tel2=tel2, email=email)

        n_cliente.endereco.append(n_endereco)
        n_cliente.contato.append(n_contato)
        db.session.add(n_cliente)
        db.session.commit()

        return redirect(url_for('core.lista_clientes'))

    return render_template('cadastro_clientes.html', form=form)
