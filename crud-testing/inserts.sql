INSERT INTO CLIENTE VALUES(NULL,'ANTONIO','M',NULL,'78558-6');

insert into t_dono values(null,'Amanda', 'F');
insert into t_dono values(null,'Aline', 'F');
insert into t_dono values(null,'Talu', 'F');
insert into t_dono values(null,'Júlio', 'M');



insert into t_dogs values(null,'Puka', 'shitsu', 'longo', 4, '2016-10-01', 'F', 'sim', 3);

insert into t_dogs values(null,'Kate', 'shitsu', 'longo', 5, '2016-10-01', 'F', 'sim', 2);
insert into t_dogs values(null,'Neguinha', 'shitsu', 'longo', 3, '2016-10-01', 'F', 'sim', 2);
insert into t_dogs values(null,'Sansa', 'spitz', 'longo', 3, '2016-10-01', 'F', 'sim', 2);
insert into t_dogs values(null,'Thobias', 'pug', 'curto', 3, '2016-10-01', 'M', 'sim', 4);
insert into t_dogs values(null,'Nina', 'shitsu', 'longo', 3, '2017-10-01', 'F', 'sim', 1);


insert into t_telefone values(null,'11-98183-6620', 2);
insert into t_telefone values(null,'11-95276-2922', 2);
insert into t_telefone values(null,'11-91010-1111', 3);
insert into t_telefone values(null,'11-91010-1111', 1);
insert into t_telefone values(null,'11-91010-1111', 4);

insert into t_adress values(null,'Irlanda 554', 'Capuava', 'Santo André', null, 0, 2);

update t_adress
set estado = 'SP'
where dono_id = 3;

insert into t_adress values(null,'teste','teste','teste', 'BA', 3000, 4);
insert into t_adress values(null,'Irlanda 554', 'Capuava', 'Santo André', 'SP', 0, 2);
insert into t_adress values(null,'teste','teste','teste', 'MA', 4000, 1);
insert into t_adress values(null,'teste','teste','teste', 'CE', 3500, 3);

delete from t_adress
where dono_id = 3;

select * from t_adress;

insert into t_venda values(null,'teste','2018-01-01', 2, 120, 'avulso', 0, 'cash', '2018-01-01', 120, 1);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 1);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 2);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 3);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 5);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 6);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 4);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 3);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 3);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 2);
insert into t_venda values(null,'teste','2018-02-14', 2, 120.99, 'avulso', 0, 'cash', '2018-02-14', 120.99, 1);
insert into t_venda values(null,'teste','2018-03-22', 2, 120.99, 'avulso', 0, 'cash', '2018-03-22', 120.99, 4);
insert into t_venda values(null,'teste','2018-03-22', 2, 120.99, 'avulso', 0, 'cash', '2018-03-22', 120.99, 5);
insert into t_venda values(null,'teste','2018-01-01', 2, 120, 'avulso', 0, 'cash', '2018-01-01', 120, 5);
insert into t_venda values(null,'teste','2018-03-22', 2, 120.99, 'avulso', 0, 'cash', '2018-03-22', 120.99, 6);
insert into t_venda values(null,'teste','2018-03-22', 2, 120.99, 'avulso', 0, 'cash', '2018-03-22', 120.99, 2);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 1);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 2);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 3);
insert into t_venda values(null,'teste','2018-07-02', 2, 120.99, 'avulso', 0, 'cash', '2018-03-30', 120.99, 4);
insert into t_venda values(null,'teste','2018-07-02', 2, 120.99, 'avulso', 0, 'cash', '2018-07-02', 120.99, 5);
insert into t_venda values(null,'teste','2018-07-02', 2, 120.99, 'avulso', 0, 'cash', '2018-07-02', 120.99, 6);
insert into t_venda values(null,'teste','2018-07-02', 2, 120.99, 'avulso', 0, 'cash', '2018-07-02', 120.99, 1);
insert into t_venda values(null,'teste','2018-07-02', 2, 120.99, 'avulso', 0, 'cash', '2018-07-02', 120.99, 6);
insert into t_venda values(null,'teste','2018-07-02', 2, 120.99, 'avulso', 0, 'cash', '2018-07-02', 120.99, 7);
insert into t_venda values(null,'teste','2018-07-02', 2, 120.99, 'avulso', 0, 'cash', '2018-07-02', 120.99, 2);
insert into t_venda values(null,'teste','2018-01-01', 2, 120, 'avulso', 0, 'cash', '2018-01-01', 120, 2);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 3);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 3);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 4);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 4);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 5);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 5);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 6);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 6);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 1);
insert into t_venda values(null,'teste','2018-09-15', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 2);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 2);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 2);
insert into t_venda values(null,'teste','2018-01-01', 2, 120, 'avulso', 0, 'cash', '2018-01-01', 120, 1);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 5);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-09-15', 120.99, 5);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 5);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-01-07', 120.99, 6);
insert into t_venda values(null,'teste','2018-08-30', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 6);
insert into t_venda values(null,'teste','2018-08-30', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 6);
insert into t_venda values(null,'teste','2018-08-30', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 4);
insert into t_venda values(null,'teste','2018-08-30', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 4);
insert into t_venda values(null,'teste','2018-08-30', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 4);
insert into t_venda values(null,'teste','2018-08-30', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 2);
insert into t_venda values(null,'teste','2018-08-30', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 2);
insert into t_venda values(null,'teste','2018-01-07', 2, 120.99, 'avulso', 0, 'cash', '2018-08-30', 120.99, 5);
