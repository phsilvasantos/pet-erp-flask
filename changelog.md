# Project roadmap

## todo

- insert records, ssh side
    - build scripts to do that - done!

- testing
- buying a domain



2018-12-04
- launch aws
- test extracting data through remote
- add api
- modificar registros
- listagem após delecao de vendas / pagamentos
- origem ok : alertas / últimas vendas /
    - excluir peludo: com problemas
- listar últimos banhos para peludos - ok
- listar caes para cada dono - ok
- listagem de caes para dono - incluir cao para este dono - not
- botao ver dono para peludo - ok




2018-12-04
- listema de login e db para cada user - ok
- launch aws
- test extracting data through remote
- add api
- modificar registros
- testing - cadastro looks good - ok
- testing vendas - ok



2018-12-03
- testing - cadastro looks good
- testing vendas
- add api
- launch aws
- modificar registros
- listema de login e db para cada user
- fix paginador - ok
- pagamentos valor 0 - ok
- validacao nos campos - ok
- layout dos botoes - ok
- adicionar detalhes para peludos / para vendas - ok
- sort lista de clientes quando for cadastrar novo peludo - por nome - ok
- lista de clientes - botao para incluir cachorro - ok
- botao ùltimas compras - ok
- botao nova venda para cliente x - ok
- detalhes de vendas - remover botao add $$$ qdo saldo > 0 - ok
- teste para valor de entrada acima do saldo - ok



2018-11-29
- testing
- add api
- launch aws
- modificar registros
- better details - halfway - add dogs
- listema de login e db para cada user
- fix paginador
- pagamentos valor 0
- validacao nos campos
- adicionar aviso para exclusão - ok
- form clientes - ok
- fix registro de novos clientes - sem contato e endereço? - ok
- fix add dogs - ok
- layout dos botoes
- lista de clientes - botao para incluir cachorro
- adicionar detalhes para peludos / para vendas
- testar funcionamento dos parents/children
- sort lista de clientes quando for cadastrar novo peludo
- problema listagem de peludos - último botao - all ok
- id não atribuido para cadastro de novos caes...  - ok

2018-11-28
- create readme - ok
- testing
- add api
- launch aws
- modificar registros
- better detais - halfway
- listema de login e db para cada user
- fix paginador
- pagamentos valor 0
- validacao nos campos
- adicionar aviso para exclusão
- consertar calculo de idade para null - ok


2018-11-26
- zerar db, tirar do git hub - ok
- model cliente real - ok
- adicionar dados excel - ok
- add api
- launch aws
- modificar registros
- adicionar dados reais do excel - ok
- listema de login e db para cada user
- fix paginador
- pagamentos valor 0
- validacao nos campos


2018-11-24
- excluir clientes ok
- excluir pagamentos - ok
- excluir vendas - ok
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
