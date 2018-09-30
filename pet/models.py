"""As tabelas do db."""
from pet import db


class cliente(db.Model):
    """O dono do cachorro."""

    # Create a table in the db
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.NVARCHAR(30), nullable=False)
    sexo = db.Column(db.Enum('M', 'H'), nullable=False)
    cachorro = db.relationship("cachorro")

    def __init__(self, nome, sexo):
        """Cria a entidade."""
        self.nome = nome
        self.sexo = sexo

    def __repr__(self):
        """Representação."""
        return f"Cliente: {self.nome}, sexo: {self.sexo}"


class cachorro(db.Model):
    """O cachorro."""

    # Create a table in the db
    __tablename__ = 'cachorro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.NVARCHAR(30), nullable=False)
    breed = db.Column(db.NVARCHAR(20), nullable=False)
    pelagem = db.Column(db.Enum('longo', 'curto'), nullable=False)
    idade = db.Column(db.Integer, nullable=True)
    data_start = db.Column(db.Date, nullable=True)
    sexo = db.Column(db.Enum('M', 'F'), nullable=False)
    castrado = db.Column(db.Enum('S', 'N'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    def __init__(self, nome, breed, pelagem, idade, start, sexo, castrado):
        """Cria a entidade."""
        self.nome = nome
        self.breed = breed
        self.pelagem = pelagem
        self.idade = idade
        self.data_start = start
        self.sexo = sexo
        self.castrado = castrado
        # self.cliente_id = cliente_id

    def __repr__(self):
        """Representação."""
        return f"""
        {self.nome}, um {self.breed} de pelo {self.pelagem}
        dono: {self.cliente_id}
        """



# create table t_adress (
#     id_adress int primary key auto_increment,
#     rua varchar(30) not null,
#     cidade varchar(15) not null,
#     estado char(2) default 'SP',
#     distancia_pet int,
#     dono_id int unique
# );
#
# alter table t_adress
# add column bairro varchar(20)
# after rua;
#
#
# create table t_telefone (
#     id_telefone int primary key auto_increment,
#     numero int,
#     dono_id int
# );
#
# alter table t_telefone
# modify numero varchar(15);
#
# create table t_venda (
#     id_venda int auto_increment,
#     description varchar(30) not null,
#     data date not null,
#     n_banhos int default 1,
#     valor_venda decimal(10,2),
#     tipo enum('pacote','avulso') not null,
#     valor_taxi decimal(10,2) default 0,
#     forma_pagto enum('cash','credito', 'debito', 'cheque') not null,
#     data_pagto date,
#     valor_entrada decimal(10,2),
#     dog_id int,
#     primary key(id_venda, dog_id)
# );
#
# alter table t_dogs add constraint fk_dono_dogs
# foreign key(dono_id)
# references t_dono(id_dono);
#
# alter table t_adress add constraint fk_dono_adress
# foreign key(dono_id)
# references t_dono(id_dono);
#
# alter table t_telefone add constraint fk_dono_telefone
# foreign key(dono_id)
# references t_dono(id_dono);
#
# alter table t_venda add constraint fk_dog_venda
# foreign key(dog_id)
# references t_dogs(id_dog);
