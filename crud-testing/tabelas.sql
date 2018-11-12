create database pet;
use pet;


create table t_dono (
    id_dono int primary key auto_increment,
    nome varchar(30) not null,
    sexo enum('M','F') not null
);

create table t_dogs (
    id_dog int auto_increment,
    dog varchar(20) not null,
    breed varchar(10) not null,
    pelagem enum('longo','curto') not null,
    idade int,
    data_start date,
    sexo enum('M','F') not null,
    castrado enum('sim','não') not null,
    dono_id int not null,
    primary key(id_dog, dono_id)
);



create table t_adress (
    id_adress int primary key auto_increment,
    rua varchar(30) not null,
    cidade varchar(15) not null,
    estado char(2) default 'SP',
    distancia_pet int,
    dono_id int unique
);

alter table t_adress
add column bairro varchar(20)
after rua;


create table t_telefone (
    id_telefone int primary key auto_increment,
    numero int,
    dono_id int
);

alter table t_telefone
modify numero varchar(15);

create table t_venda (
    id_venda int auto_increment,
    description varchar(30) not null,
    data date not null,
    n_banhos int default 1,
    valor_venda decimal(10,2),
    tipo enum('pacote','avulso') not null,
    valor_taxi decimal(10,2) default 0,
    forma_pagto enum('cash','credito', 'debito', 'cheque') not null,
    data_pagto date,
    valor_entrada decimal(10,2),
    dog_id int,
    primary key(id_venda, dog_id)
);

alter table t_dogs add constraint fk_dono_dogs
foreign key(dono_id)
references t_dono(id_dono);

alter table t_adress add constraint fk_dono_adress
foreign key(dono_id)
references t_dono(id_dono);

alter table t_telefone add constraint fk_dono_telefone
foreign key(dono_id)
references t_dono(id_dono);

alter table t_venda add constraint fk_dog_venda
foreign key(dog_id)
references t_dogs(id_dog);
