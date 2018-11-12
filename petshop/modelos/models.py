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
    venda = db.relationship('Vendas', backref='clientes', lazy=True)
    contato = db.relationship('Contatos')
    endereco = db.relationship('Enderecos')

    def lista_peludos(self):
        """Lista os cães deste cliente."""
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

    venda = db.relationship('Vendas', backref='peludos', lazy=True)

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


class Vendas(db.Model):
    """
    Cadastro de Vendas - todos os tipos.

    descricao, data_venda, data_pbanho,
    valor_servicos, valor_taxi, n_banhos, tipo, pacote
    """

    __tablename__ = 'vendas'

    # comum
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.NVARCHAR(10), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    valor_servicos = db.Column(db.Float, nullable=True)
    valor_taxi = db.Column(db.Float, nullable=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    peludo_id = db.Column(db.Integer, db.ForeignKey('peludos.id'))
    pagamentos = db.relationship('Pagamentos')

    # banho e tosa
    data_pbanho = db.Column(db.Date, nullable=True)
    n_banhos = db.Column(db.Integer, nullable=True)
    tipo_banho = db.Column(db.Enum('pacote', 'avulso', 'cortesia'), nullable=True)
    pacote = db.Column(db.NVARCHAR(10), nullable=True)

    # hospedagem
    data_entrada = db.Column(db.Date, nullable=True)
    data_saida = db.Column(db.Date, nullable=True)
    valor_diarias = db.Column(db.Float, nullable=True)

    # produtos
    valor_prod = db.Column(db.Float, nullable=True)
    custo_prod = db.Column(db.Float, nullable=True)

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
        {self.descricao}, em {self.data_venda} no valor de {self.valor_servicos}
        para {Clientes.query.get(self.cliente_id).nome}
        Saldo: R${self.saldo()}
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
    # tipo_venda = db.Column(
    #     db.Enum('banhos', 'hospedagens', 'cursos', 'produtos', 'outros'), nullable=False)
    forma_pagto = db.Column(
        db.Enum('cash', 'debito', 'credito', 'cheque', 'pendente'), nullable=False)
    # # data_pagto = db.Column(db.Date, nullable=False)
    # valor_entrada = db.Column(db.Numeric, nullable=False)
    venda_id = db.Column(db.Integer, db.ForeignKey('vendas.id'))
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
