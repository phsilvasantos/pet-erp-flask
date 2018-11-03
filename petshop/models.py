from petshop import db
import datetime as dt


class Clientes(db.Model):
    """O dono do peludo."""

    # Create a table in the db
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.NVARCHAR(30), nullable=False)
    sexo = db.Column(db.Enum('M', 'H'), nullable=False)
    peludo = db.relationship('Peludos')
    contato = db.relationship('Contatos')
    endereco = db.relationship('Enderecos')
    venda = db.relationship('Vendas')

    def __init__(self, nome, sexo):
        """Cria a entidade - nome, sexo."""
        self.nome = nome
        self.sexo = sexo

    def __repr__(self):
        """Representação."""
        return f"{self.nome}, da {self.endereco[0]} - tel {self.contato[0]}"


class Peludos(db.Model):
    """O peludo."""

    __tablename__ = 'peludos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.NVARCHAR(30), nullable=False)
    breed = db.Column(db.NVARCHAR(20), nullable=False)
    pelagem = db.Column(db.Enum('longo', 'curto'), nullable=False)
    nascimento = db.Column(db.Date, nullable=True)
    data_start = db.Column(db.Date, nullable=True)
    sexo = db.Column(db.Enum('M', 'F'), nullable=False)
    castrado = db.Column(db.Enum('S', 'N'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    venda = db.relationship('Vendas')
    # cliente = db.relationship('Cliente', back_populates='peludo')
    # venda = db.relationship('Venda', back_populates='peludo')

    def __init__(self, nome, breed, pelagem, nascimento, start, sexo, castrado):
        """
        Cria a entidade.

        nome, breed, pelagem, nascimento, start, sexo, castrado
        """
        self.nome = nome
        self.breed = breed
        self.pelagem = pelagem
        self.nascimento = nascimento
        self.data_start = start
        self.sexo = sexo
        self.castrado = castrado

    def __repr__(self):
        """Representação."""
        diff = dt.date.today() - self.nascimento
        idade = round(diff.days/365, 2)
        return f"""
        {self.nome}, um {self.breed} de pelo {self.pelagem} com {idade} anos
        cliente: {Clientes.query.get(self.cliente_id).nome}
        """


class Enderecos(db.Model):
    """Rua, numero, bairro, cidade, estado, distancia."""

    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.NVARCHAR(30))
    numero = db.Column(db.Integer)
    bairro = db.Column(db.NVARCHAR(30))
    cidade = db.Column(db.NVARCHAR(30))
    estado = db.Column(db.CHAR(2))
    distancia = db.Column(db.Numeric)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    # cliente = db.relationship('Cliente', back_populates='endereco')

    def _init_(self, rua, numero, bairro, cidade, estado, distancia):

        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.distancia = distancia

    def __repr__(self):
        """Representação."""
        return f"{self.rua}, {self.numero} em {self.cidade}"


class Contatos(db.Model):
    """The contacts."""

    __tablename__ = 'contatos'

    id = db.Column(db.Integer, primary_key=True)
    tel1 = db.Column(db.NVARCHAR(13))
    tel2 = db.Column(db.NVARCHAR(13))
    email = db.Column(db.NVARCHAR(30))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    # cliente = db.relationship('Cliente', back_populates='contato')

    def _init_(self, tel1, tel2, email):
        """Tel1, tel2, email."""
        self.tel1 = tel1
        self.tel2 = tel2
        self.email = email

    def __repr__(self):
        """Representação."""
        return f"""
        {self.tel1}, {self.email}
        """


class Vendas(db.Model):
    """
    Cadastro de Vendas

    descricao, data_venda, valor_venda, valor_taxi, n_banhos,
    tipo, pacote, forma_pagto, data_pagto, valor_entrada
    """
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    valor_venda = db.Column(db.Numeric, nullable=False)
    valor_taxi = db.Column(db.Numeric, nullable=False)
    n_banhos = db.Column(db.INT, nullable=False)
    tipo = db.Column(db.Enum('pacote', 'avulso'), nullable=False)
    pacote = db.Column(db.NVARCHAR(10), nullable=False)
    forma_pagto = db.Column(
        db.Enum('cash', 'debito', 'credito', 'cheque', 'pendente'), nullable=False)
    data_pagto = db.Column(db.Date, nullable=False)
    valor_entrada = db.Column(db.Numeric, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    # cliente = db.relationship('Cliente', back_populates='venda')
    peludo_id = db.Column(db.Integer, db.ForeignKey('peludos.id'))
    # peludo = db.relationship('Peludo', back_populates='venda')

    def _init_(
        self, descricao, data_venda, valor_venda, valor_taxi, n_banhos,
        tipo, pacote, forma_pagto, data_pagto, valor_entrada
            ):

        self.descricao = descricao
        self.data_venda = data_venda
        self.valor_venda = valor_venda
        self.valor_taxi = valor_taxi
        self.n_banhos = n_banhos
        self.tipo = tipo
        self.pacote = pacote
        self.forma_pagto = data_pagto
        self.data_pagto = forma_pagto
        self.valor_entrada = valor_entrada

    def __repr__(self):
        """Representação."""
        return f"""
        {self.descricao}, em {self.data_venda} no valor de {self.valor_venda}
        """
