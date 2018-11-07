from petshop import db
import datetime as dt
import numpy as np

class Clientes(db.Model):
    """O dono do peludo."""

    # Create a table in the db
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.NVARCHAR(30), nullable=False)
    sexo = db.Column(db.Enum('M', 'H'), nullable=False)

    peludo = db.relationship('Peludos', backref='clientes', lazy=True)
    venda_bt = db.relationship('Vendas_bt', backref='clientes', lazy=True)
    venda_hot = db.relationship('Vendas_hot', backref='clientes', lazy=True)
    venda_cur = db.relationship('Vendas_cur', backref='clientes', lazy=True)
    venda_prod = db.relationship('Vendas_prod', backref='clientes', lazy=True)
    contato = db.relationship('Contatos')
    endereco = db.relationship('Enderecos')

    def lista_peludos(self):
        """Lista os cães deste cliente."""
        # caes_cliente = Clientes.query.filter_by(nome=self.nome).first().peludo
        caes_cliente = self.peludo
        caes_cliente = [i.nome for i in caes_cliente]
        if caes_cliente:
            texto = ' e '.join(caes_cliente)
            return f'dono de {texto}'
        return 'sem peludos ainda'

    def __init__(self, nome, sexo):
        """Cria a entidade - nome, sexo."""
        self.nome = nome
        self.sexo = sexo

    def __repr__(self):
        """Representação."""
        return f"""
        {self.nome}, da {self.endereco[0]} - tel {self.contato[0]}
        {self.lista_peludos()}
        """


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

    venda_bt = db.relationship('Vendas_bt', backref='peludos', lazy=True)
    venda_hot = db.relationship('Vendas_hot', backref='peludos', lazy=True)

    def get_idade(self):
        """Calcula a idade."""
        diff = dt.date.today() - self.nascimento
        return round(diff.days/365, 2)

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
        return f"""
        {self.nome}, um {self.breed} de pelo {self.pelagem} com {self.get_idade()} anos
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
    distancia = db.Column(db.Float)
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


class Vendas_bt(db.Model):
    """
    Cadastro de Vendas de banho e tosa.

    descricao, data_venda, data_pbanho,
    valor_servicos, valor_taxi, n_banhos, tipo, pacote
    """

    __tablename__ = 'vendas_bt'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    data_pbanho = db.Column(db.Date, nullable=False)
    valor_servicos = db.Column(db.Float, nullable=False)
    valor_taxi = db.Column(db.Float, nullable=False)
    n_banhos = db.Column(db.Integer, nullable=False)
    tipo_banho = db.Column(db.Enum('pacote', 'avulso', 'cortesia'), nullable=False)
    pacote = db.Column(db.NVARCHAR(10), nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    peludo_id = db.Column(db.Integer, db.ForeignKey('peludos.id'))

    pagamentos = db.relationship('Pagamentos')

    def saldo(self):
        """Calcula o saldo desta venda."""
        valor_total = self.valor_servicos + self.valor_taxi
        pagamentos = self.pagamentos
        if pagamentos:
            valores_pagos = [item.valor for item in pagamentos]
            valores_pagos = np.array(valores_pagos)
            saldo = valor_total - valores_pagos.sum()
            return saldo

        return valor_total

    def _init_(
        self, descricao, data_venda, data_pbanho,
        valor_servicos, valor_taxi, n_banhos, tipo_banho, pacote
            ):

        self.descricao = descricao
        self.data_venda = data_venda
        self.data_pbanho = data_pbanho
        self.valor_servicos = valor_servicos
        self.valor_taxi = valor_taxi
        self.n_banhos = n_banhos
        self.tipo_banho = tipo_banho
        self.pacote = pacote
        self.saldo = self.saldo()

    def __repr__(self):
        """Representação."""
        return f"""
        {self.descricao}, em {self.data_venda} no valor de {self.valor_servicos}
        para {Clientes.query.get(self.cliente_id).nome}
        Saldo: R${self.saldo()}
        """


class Vendas_hot(db.Model):
    """
    Cadastro de Vendas de hospedagem.

    descricao, data_venda, data_entrada, data_saida,
    valor_diarias, valor_servicos, valor_taxi
    """

    __tablename__ = 'vendas_hot'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    data_entrada = db.Column(db.Date, nullable=False)
    data_saida = db.Column(db.Date, nullable=False)
    valor_diarias = db.Column(db.Float, nullable=False)
    valor_servicos = db.Column(db.Float, nullable=False)
    valor_taxi = db.Column(db.Float, nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    peludo_id = db.Column(db.Integer, db.ForeignKey('peludos.id'))

    pagamentos = db.relationship('Pagamentos')

    def _init_(
        self, descricao, data_venda, data_entrada, data_saida,
        valor_diarias, valor_servicos, valor_taxi
            ):

        self.descricao = descricao
        self.data_venda = data_venda
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.valor_diarias = valor_diarias
        self.valor_servicos = valor_servicos
        self.valor_taxi = valor_taxi

    def __repr__(self):
        """Representação."""
        return f"""
        {self.descricao}, em {self.data_venda} no valor de {self.valor_diarias}
        para {Clientes.query.get(self.cliente_id).nome}
        """


class Vendas_cur(db.Model):
    """
    Cadastro de Vendas de cursos.

    descricao, data_venda, data_entrada, valor_servicos
    """

    __tablename__ = 'vendas_cur'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    data_entrada = db.Column(db.Date, nullable=False)
    valor_servicos = db.Column(db.Float, nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

    pagamentos = db.relationship('Pagamentos')

    def _init_(self, descricao, data_venda, data_entrada, valor_servicos):

        self.descricao = descricao
        self.data_venda = data_venda
        self.data_entrada = data_entrada
        self.valor_servicos = valor_servicos

    def __repr__(self):
        """Representação."""
        return f"""
        {self.descricao}, em {self.data_venda} no valor de {self.valor_servicos}
        para {Clientes.query.get(self.cliente_id).nome}
        """


class Vendas_prod(db.Model):
    """
    Cadastro de Vendas de produtos.

    descricao, data_venda, valor
    """

    __tablename__ = 'vendas_prod'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

    pagamentos = db.relationship('Pagamentos')

    def _init_(self, descricao, data_venda, valor):

        self.descricao = descricao
        self.data_venda = data_venda
        self.valor = valor

    def __repr__(self):
        """Representação."""
        return f"""
        {self.descricao}, em {self.data_venda} no valor de {self.valor}
        para {Clientes.query.get(self.cliente_id).nome}
        """


class Pagamentos(db.Model):
    """
    Cadastro de pagamentos.

    data, valor, forma_pagto, valor_entrada
    """

    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    valor_entrada = db.Column(db.Float, nullable=False)
    # tipo_venda = db.Column(
    #     db.Enum('banhos', 'hospedagens', 'cursos', 'produtos', 'outros'), nullable=False)
    forma_pagto = db.Column(
        db.Enum('cash', 'debito', 'credito', 'cheque', 'pendente'), nullable=False)
    # # data_pagto = db.Column(db.Date, nullable=False)
    # valor_entrada = db.Column(db.Numeric, nullable=False)
    venda_bt_id = db.Column(db.Integer, db.ForeignKey('vendas_bt.id'))
    venda_hot_id = db.Column(db.Integer, db.ForeignKey('vendas_hot.id'))
    venda_cur_id = db.Column(db.Integer, db.ForeignKey('vendas_cur.id'))
    venda_pro_id = db.Column(db.Integer, db.ForeignKey('vendas_prod.id'))
    # PrimaryKeyConstraint('id', 'version_id', name='mytable_pk')

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
        Pagamento em {self.data} no valor de {self.valor}
        """
