from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_clientes, Form_peludos
from petshop.modelos.models import Clientes, Peludos, Contatos, Enderecos, Vendas

views_cadastros = Blueprint('views_cadastros', __name__)


@views_cadastros.route('/cadastro_clientes/<operacao>/<int:id>',
                       methods=['GET', 'POST'])
def cadastro_clientes(operacao, id):
    """Cadastra / modifica clientes."""
    # operacoes: cadastrar, modificar
    if operacao == 'cadastrar':
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

            return redirect(url_for('views_consultas.listagens', id=0, tipo='clientes'))
        return render_template('cadastro_clientes.html', form=form)

    if operacao == 'ver_vendas':
        page = request.args.get('page', 1, type=int)
        listagem = Vendas.query.filter(Vendas.cliente_id == id).paginate(page=page, per_page=5)
        tipo = 'vendas'
        heading = 'Últimas vendas'
        return render_template('listagens.html', listagem=listagem,
                               heading=heading, tipo=tipo)


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

        return redirect(url_for('views_consultas.listagens', id=0, tipo='peludos'))

    return render_template('cadastro_peludos.html', form=form)
