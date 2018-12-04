from flask import render_template, request, Blueprint, redirect, url_for
from petshop import db
from petshop.modelos.forms import Form_clientes, Form_peludos
from petshop.modelos.models import Clientes, Peludos, Contatos, Enderecos, Vendas, Pagamentos

views_cadastros = Blueprint('views_cadastros', __name__)


@views_cadastros.route('/cadastro_clientes/',
                       methods=['GET', 'POST'])
def cadastro_clientes():
    """Cadastra / modifica clientes."""
    form = Form_clientes()

    if form.validate_on_submit():
        bairro = form.bairro.data
        cep = form.cep.data
        cidade = form.cidade.data
        complemento = form.complemento.data
        distancia = form.distancia.data
        email = form.email.data
        estado = form.estado.data
        id = form.id.data
        nascimento = form.nascimento.data
        nome = form.nome.data
        numero = form.numero.data
        profissao = form.profissao.data
        rua = form.rua.data
        sexo = form.sexo.data
        tel1 = form.tel1.data
        tel2 = form.tel2.data

        # db part
        n_cliente = Clientes(id=id, nome=nome, sexo=sexo,
                             profissao=profissao, nascimento=nascimento)

        n_endereco = Enderecos(rua=rua,
                               numero=numero,
                               complemento=complemento,
                               bairro=bairro,
                               cidade=cidade,
                               estado=estado,
                               cep=cep,
                               distancia=distancia,
                               cliente_id=id)

        n_contato = Contatos(tel1=tel1, tel2=tel2, email=email, cliente_id=id)

        n_cliente.endereco.append(n_endereco)
        n_cliente.contato.append(n_contato)
        db.session.add(n_cliente)
        db.session.commit()

        return redirect(url_for('views_consultas.listagens', id=0,
                                tipo='clientes'))
    return render_template('cadastro_clientes.html', form=form)


@views_cadastros.route('/cadastro_peludos', methods=['GET', 'POST'])
def cadastro_peludos():
    """Cadastra peludos."""
    cliente_id = request.args.get('id', 0, type=int)

    if cliente_id:
        clientes_cadastrados = [Clientes.query.get(cliente_id)]
    else:
        clientes_cadastrados = Clientes.query.all()

    lista_clientes = [(i.id, i.nome) for i in clientes_cadastrados]

    lista_clientes = sorted(lista_clientes, key=lambda item: item[1])

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
        n_peludo = Peludos(nome=nome,
                           breed=breed,
                           pelagem=pelagem,
                           nascimento=nascimento,
                           data_start=data_start,
                           sexo=sexo,
                           castrado=castrado)

        n_cliente = Clientes.query.get(cliente)

        # db.session.add(n_peludo)
        n_cliente.peludo.append(n_peludo)
        db.session.commit()

        return redirect(url_for('views_consultas.listagens', id=0,
                                tipo='peludos'))

    return render_template('cadastro_peludos.html', form=form)


@views_cadastros.route('/exclusao/<tipo>/<int:id>', methods=['GET', 'POST'])
def exclusao(tipo, id):
    """Exclui registro."""
    if tipo in ['vendas', 'aberto']:
        venda = Vendas.query.get(id)
        pagamentos = Pagamentos.query.filter(Pagamentos.venda_id == id).all()

        for pagto in pagamentos:
            db.session.delete(pagto)

        db.session.delete(venda)
        db.session.commit()
        return redirect(url_for('views_consultas.listagens', id=0, tipo=tipo))

    if tipo == 'clientes':
        cliente = Clientes.query.get(id)
        vendas = Vendas.query.filter(Vendas.cliente_id == id).all()
        for venda in vendas:
            pagamentos = Pagamentos.query.filter(Pagamentos.venda_id == venda.id).all()
            for pagto in pagamentos:
                if pagto:
                    db.session.delete(pagto)
            if venda:
                db.session.delete(venda)

        peludos = Peludos.query.filter(Peludos.cliente_id == id).all()
        for peludo in peludos:
            if(peludo):
                db.session.delete(peludo)

        enderecos = Enderecos.query.filter(Enderecos.cliente_id == id).all()
        for endereco in enderecos:
            if(endereco):
                db.session.delete(endereco)

        contatos = Contatos.query.filter(Contatos.cliente_id == id).all()
        for contato in contatos:
            if(contato):
                db.session.delete(contato)

        db.session.delete(cliente)
        db.session.commit()
        return redirect(url_for('views_consultas.listagens', id=0, tipo=tipo))

    if tipo == 'peludos':
        peludos = Peludos.query.get(id)
        db.session.delete(peludo)
        db.session.commit()
        return redirect(url_for('views_consultas.listagens', id=0, tipo=tipo))

    if tipo == 'd_pagamento':
        pagamento = Pagamentos.query.get(id)
        venda = Vendas.query.get(pagamento.venda_id)

        db.session.delete(pagamento)
        venda.saldo = venda.calcula_saldo()
        db.session.commit()

        return redirect(url_for('views_consultas.listagens', id=0, tipo=tipo))
