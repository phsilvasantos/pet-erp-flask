# Project roadmap

## todo

2018-11-24
- add api
- launch


## mapa lista vendas

- home > lista aberto > click item
- detalhes aberto
    - descricao
    - modificar
    - add $$$
    - listar $$$ somente se já tem

- listagem pagamentos > click item
- details d_pagamentos



2018-11-24
- excluir clientes ok
- excluir pagamentos
- excluir vendas
- modificar registros
- adicionar dados reais do excel
- api
- listema de login e db para cada user
- fix paginador
- reworked layout para listagens ok
- opção de incluir pagamentos, qdo listando pagamentos - ok
- proteger contra pagamentos maiores que o saldo - ok
- pagamentos valor 0
- validacao nos campos
- ver vendas para cada cliente - ok, mudar para views_consultas



2018-11-21
- outros tipos de venda - ok
- modificar vendas - todo
- modificar registros - todo
- opção de incluir pagamentos, qdo listando pagamentos - halfway
- api
- pagamentos valor 0
- validacao nos campos




2018-11-19
- outros tipos de venda
- consertar paginador... - ok
- modificar vendas - todo
- modificar registros - todo
- api
- wtf componentes or fields? - ok
- pagamentos valor 0
- verificar vendas sem pagamento demorando pra aparecer - ok
- validacao nos campos




2018-11-17
- listagem after cadastro cliente - ok
- listagem after cadastro peludos - ok
- botão para incluir novas vendas - ok
- relação de pagamentos para alterar - ok
- venda bt para 2 cachorros - ok
- unificar listagens - ok
- modificar vendas - todo
- modificar registros - todo
- api
- outros tipos de venda
- paginador para listagens - ok
- wtf componentes or fields?
- pagamentos valor 0
- listagem de vendas sem pagamentos / sem saldo - ok
- adicionar botao sem pagamento agora (pagar depois) - ok
- verificar vendas sem pagamento demorando pra aparecer
- validacao nos campos


2018-11-15
- adicionar pagamentos - ok
- lista somente se saldo for > 0 - ok



## structure

home    |vendas             | clientes          | Despesas      | Fornecedores | BI
        |   bt              |   Pessoas         |   Ajudantes   |
        |   hospedagem      |   Peludos         |   Compras     |
        |   cursos          |                   |   Totais      |
        |   produtos        |                   |
        |   últimas         |                   |

###  vendas

- tipo
    - listagem
        - novo
            - escolher cliente
                - cadastro de venda
                    - incluir pagamentos
                        - últimas (listagem e alteração)

- últimas (listagem e alteração)


###  clientes

- tipo
    - listagem por nome com link para detalhamento e alteração / botao para cadastrar novo


### Despesas

- tipo > lista com últimas / incluir nova
- totais - somatória por tipo (escolher mês)

### BI

- pontuação de clientes












## Changelog
