create table dono (
    id_dono int primary key auto_increment,
    nome varchar(30) not null,
    sexo enum('M','F') not null
);

create table dogs (
    id_dog int primary key auto_increment,
    dog varchar(20) not null,
    breed varchar(10) not null,
    pelagem enum('longo','curto') not null,
    idade int,
    data_start date,
    sexo enum('M','F') not null,
    castrado enum('sim','não') not null,
    dono_id int unique not null,
    foreign key(dono_id)
);


create table adress (
    id_adress int primary key auto_increment,
    rua varchar(30) not null,
    cidade varchar(15) not null,
    estado char(2) default('SP')
    distancia_pet int,
    dono_id int unique,
    foreign key(dono_id)
);

create table telefone (
    id_telefone int primary key auto_increment,
    numero int,
    dono_id int unique,
    foreign key(dono_id)
);

create table venda (
    id_venda int primary key auto_increment,
    description varchar(30) not null,
    data date not null,
    n_banhos int default(1)
    valor_venda decimal(10,2)
    tipo enum('pacote','avulso') not null,
    valor_taxi decimal(10,2) default(0)
    forma_pagto enum('cash','credito', 'debito', 'cheque') not null,
    data_pagto date,
    valor_entrada decimal(10,2)
    dog_id int unique,
    foreign key(dog_id)
);
