from werkzeug.security import generate_password_hash, check_password_hash
from petshop import db, login_manager
from flask_login import UserMixin
import datetime as dt
import numpy as np


@login_manager.user_loader
def load_user(user_id):
    """Load user."""
    return Gerentes.query.get(user_id)


class Gerentes(db.Model, UserMixin):
    """User do sistema."""

    __tablename__ = 'gerentes'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    passh = db.Column(db.String(128))

    def __init__(self, email, passw):
        """Init the class."""
        self.email = email
        self.passh = generate_password_hash(passw)


    def check_passw(self, passw):
        """Hash check"""
        return check_password_hash(self.passh, passw)


class Clientes(db.Model):
    """O dono do peludo."""

    __tablename__ = 'clientes'

    id = db.Column(db.String(15), primary_key=True)

    nome = db.Column(db.String(30), nullable=False)
    profissao = db.Column(db.String(30), nullable=True)
    sexo = db.Column(db.String(1), nullable=False)
    nascimento = db.Column(db.Date, nullable=True)

    peludo = db.relationship('Peludos', backref='clientes', lazy=True)
    venda = db.relationship('Vendas', backref='clientes', lazy=True)
    contato = db.relationship('Contatos')
    endereco = db.relationship('Enderecos')

    def lista_peludos(self):
        """Lista os cães deste cliente."""
        caes_cliente = self.peludo
        caes_cliente = [i.nome for i in caes_cliente]
        if caes_cliente:
            texto = ' | '.join(caes_cliente)
            return f'Responsável por {texto}'
        return 'sem peludos ainda'

    def __init__(self, id, nome, sexo, profissao, nascimento):
        """Cria a entidade - id, nome, sexo, profissao, nascimento."""
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.profissao = profissao
        self.nascimento = nascimento

    def __repr__(self):
        """Representação."""
        return f"""
        {self.nome}, {self.lista_peludos()} - {self.contato[0]}
        """


association_table = db.Table('association',
                             db.Column('peludos_id', db.Integer,
                                       db.ForeignKey('peludos.id')),
                             db.Column('vendas_id', db.Integer,
                                       db.ForeignKey('vendas.id'))
                             )


class Peludos(db.Model):
    """O peludo."""

    __tablename__ = 'peludos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String(20), nullable=False)
    pelagem = db.Column(db.String(6), nullable=False)
    nascimento = db.Column(db.Date, nullable=True)
    data_start = db.Column(db.Date, nullable=True)
    sexo = db.Column(db.String(1), nullable=False)
    castrado = db.Column(db.String(1), nullable=False)
    cliente_id = db.Column(db.String(15), db.ForeignKey('clientes.id'))

    vendas_on_peludo = db.relationship('Vendas', secondary=association_table,
                                       back_populates="peludos_on_venda")

    def get_idade(self):
        """Calcula a idade."""
        try:
            diff = dt.date.today() - self.nascimento
            idade = round(diff.days/365, 2)
            return f'com {idade} anos.'
        except Exception:
            return 'sem idade.'

    def __init__(self, nome, breed, pelagem, nascimento, data_start,
                 sexo, castrado):
        """
        Cria a entidade.

        nome, breed, pelagem, nascimento, start, sexo, castrado
        """
        self.nome = nome
        self.breed = breed
        self.pelagem = pelagem
        self.nascimento = nascimento
        self.data_start = data_start
        self.sexo = sexo
        self.castrado = castrado

    def __repr__(self):
        """Representação."""
        return f"""
        {self.nome}, um {self.breed} de pelo {self.pelagem} {self.get_idade()}
        Responsável: {Clientes.query.get(self.cliente_id).nome}
        """


class Enderecos(db.Model):
    """Rua, numero, bairro, cidade, estado, distancia."""

    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(30))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String(10))
    bairro = db.Column(db.String(30))
    cidade = db.Column(db.String(30))
    estado = db.Column(db.CHAR(2))
    cep = db.Column(db.String(9))
    distancia = db.Column(db.Float)
    cliente_id = db.Column(db.String(15), db.ForeignKey('clientes.id'))

    def _init_(self, rua, numero, complemento, bairro, cidade, estado, cep,
               distancia, cliente_id):

        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.distancia = distancia
        self.cliente_id = cliente_id

    def __repr__(self):
        """Representação."""
        return f"{self.rua}, {self.numero} em {self.bairro} - {self.cidade}"


class Contatos(db.Model):
    """The contacts."""

    __tablename__ = 'contatos'

    id = db.Column(db.Integer, primary_key=True)
    tel1 = db.Column(db.String(13))
    tel2 = db.Column(db.String(13))
    email = db.Column(db.String(30))
    cliente_id = db.Column(db.String(15), db.ForeignKey('clientes.id'))

    def _init_(self, tel1, tel2, email, cliente_id):
        """Tel1, tel2, email."""
        self.tel1 = tel1
        self.tel2 = tel2
        self.email = email
        self.cliente_id = cliente_id

    def __repr__(self):
        """Representação."""
        return f"""
        tel.: {self.tel1}, e-mail: {self.email}
        """


class Vendas(db.Model):
    """
    Cadastro de Vendas - todos os tipos.

    descricao, data_venda, data_pbanho,
    valor_servicos, valor_taxi, n_banhos, tipo, pacote
    """

    __tablename__ = 'vendas'

    # comum
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    valor_servicos = db.Column(db.Float, nullable=True)
    valor_taxi = db.Column(db.Float, nullable=True)
    cliente_id = db.Column(db.String(15), db.ForeignKey('clientes.id'))
    peludos_on_venda = db.relationship(
        "Peludos",
        secondary=association_table,
        back_populates="vendas_on_peludo")
    saldo = db.Column(db.Float, nullable=True)
    pagamentos = db.relationship('Pagamentos')

    # banho e tosa
    data_pbanho = db.Column(db.Date, nullable=True)
    n_banhos = db.Column(db.Integer, nullable=True)
    tipo_banho = db.Column(db.String(15), nullable=True)
    pacote = db.Column(db.String(10), nullable=True)

    # hospedagem
    data_entrada = db.Column(db.Date, nullable=True)
    data_saida = db.Column(db.Date, nullable=True)
    valor_diarias = db.Column(db.Float, nullable=True)

    # produtos
    valor_prod = db.Column(db.Float, nullable=True)
    custo_prod = db.Column(db.Float, nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)

    def calcula_saldo(self, tipo='saldo'):
        """Calcula o saldo desta venda."""
        valor_total = (
                    (self.valor_servicos or 0)
                    + (self.valor_taxi or 0)
                    + (self.valor_diarias or 0)
                    + (self.valor_prod or 0)
                    )

        if tipo != 'total':
            if self.pagamentos:
                valores_pagos = [item.valor for item in self.pagamentos]
                valores_pagos = np.array(valores_pagos)
                saldo = round(valor_total - valores_pagos.sum(), 2)
                return saldo
            else:
                return valor_total

        return valor_total

    def _init_(
                self,
                custo_prod=np.nan,
                data_entrada=np.nan,
                data_pbanho=np.nan,
                data_saida=np.nan,
                data_venda=np.nan,
                descricao='uma venda',
                n_banhos=np.nan,
                pacote=np.nan,
                tipo_banho=np.nan,
                tipo='bt',
                valor_diarias=np.nan,
                valor_prod=np.nan,
                valor_servicos=np.nan,
                valor_taxi=np.nan,
            ):

        self.custo_prod = custo_prod
        self.data_entrada = data_entrada
        self.data_pbanho = data_pbanho
        self.data_saida = data_saida
        self.data_venda = data_venda
        self.descricao = descricao
        self.n_banhos = n_banhos
        self.pacote = pacote
        self.tipo = tipo
        self.tipo_banho = tipo_banho
        self.valor_diarias = valor_diarias
        self.valor_prod = valor_prod
        self.valor_servicos = valor_servicos
        self.valor_taxi = valor_taxi
        self.saldo = self.saldo()

    def __repr__(self):
        """Representação."""
        return f"""
        {self.descricao}, em {self.data_venda} no valor de
        {self.calcula_saldo(tipo='total')} para
        {Clientes.query.get(self.cliente_id).nome}
        - saldo: R${self.calcula_saldo()}
        """


class Pagamentos(db.Model):
    """
    Cadastro de pagamentos.

    data, valor, forma_pagto, valor, valor_entrada, forma_pagto
    """

    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    valor_entrada = db.Column(db.Float, nullable=False)
    forma_pagto = db.Column(
        db.String(15), nullable=False)
    venda_id = db.Column(db.Integer, db.ForeignKey('vendas.id'))

    def _init_(
        self, data, valor, valor_entrada, forma_pagto
            ):

        self.data = data
        self.valor = valor
        self.valor_entrada = valor_entrada
        self.forma_pagto = forma_pagto

    def __repr__(self):
        """Representação."""
        return f"""
        Pagamento em {self.data}, por {self.forma_pagto},
        no valor de {self.valor}
        """


# def init_db():
#     """Create all tables."""
#     db.create_all()


if __name__ == '__main__':
    init_db()
