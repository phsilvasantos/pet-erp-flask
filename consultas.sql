select d.dog, d.breed, v.valor_entrada as valor, v.data, v.forma_pagto, o.nome, t.numero, a.estado
from t_dogs d
    join t_venda v
    on d.id_dog = v.dog_id
        join t_dono o
        on o.id_dono = d.dono_id
            join t_telefone t
            on t.dono_id = o.id_dono
                join t_adress a
                on a.dono_id = o.id_dono;



select * from t_dogs;
select * from t_dono


update t_dogs
set dono_id = 2
where id_dog =1;


update t_dogs
set dono_id = 1
where dono_id = 2;


select d.dog, o.nome
from t_dogs d
    join t_dono o
    on d.dono_id = o.id_dono;


select d.dog, d.breed, v.valor_entrada as valor, v.data, v.forma_pagto, o.nome, t.numero, a.estado
from t_dogs d
    join t_venda v
    on d.id_dog = v.dog_id
        join t_dono o
        on o.id_dono = d.dono_id
            join t_telefone t
            on t.dono_id = o.id_dono
                join t_adress a
                on a.dono_id = o.id_dono
where v.data between '2018-06-01' and '2018-09-01'
order by v.data desc;




select res.breed as breed, count(res.breed) as contagem, sum(res.valor) as total from
    (select d.dog, d.breed, v.valor_entrada as valor, v.data, v.forma_pagto, o.nome, t.numero, a.estado
    from t_dogs d
        join t_venda v
        on d.id_dog = v.dog_id
            join t_dono o
            on o.id_dono = d.dono_id
                join t_telefone t
                on t.dono_id = o.id_dono
                    join t_adress a
                    on a.dono_id = o.id_dono
    where v.data between '2018-06-01' and '2018-09-01') res
group by res.breed;
