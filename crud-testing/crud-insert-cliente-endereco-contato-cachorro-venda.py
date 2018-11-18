"""Testing crud."""
from petshop import db
from petshop.modelos.models import Clientes, Peludos, Contatos, Enderecos, Vendas
from datetime import datetime
import pandas as pd



contato_info = Contatos(
                        tel1='11-95276-2922',
                        tel2='11-98183-6620',
                        email='aline.medeiros03@gmail.com'
                        )

endereco_info = Enderecos(
                        rua='Rua Irlanda', numero=554,
                        bairro='Capuava', cidade='Santo André',
                        estado='SP', distancia=0
                        )


cao_info = Peludos(
                    'Puka', 'shitzu', 'longo',
                    datetime(2014, 3, 1),
                    datetime(2016, 10, 1), 'F', 'S'
                    )


cliente_info = Clientes('Aline', 'M')

cliente_info.contato.append(contato_info)
cliente_info.endereco.append(endereco_info)
cliente_info.peludo.append(cao_info)

db.session.add(cliente_info)
db.session.commit()
# db.session.rollback()

##

contato_info = Contatos(
                        tel1='11-testeMarcelo',
                        tel2='11-testeMarcelo-2',
                        email='marcelo@gmail.com'
                        )

endereco_info = Enderecos(
                        rua='Rua Marcelo', numero=666,
                        bairro='Bairro Marcelo', cidade='Calgary',
                        estado='AL', distancia=10000
                        )


cao_info = Peludos(
                    'Leon', 'bull-terrier', 'longo',
                    datetime(2008, 1, 1),
                    datetime(2018, 10, 1), 'M', 'S'
                    )


cao_info2 = Peludos(
                    'Pipoca', 'unk', 'curto',
                    datetime(2008, 2, 1),
                    datetime(2018, 10, 2), 'F', 'S'
                    )

cliente_info = Clientes('Marcelo', 'H')

cliente_info.contato.append(contato_info)
cliente_info.endereco.append(endereco_info)
cliente_info.peludo.extend([cao_info, cao_info2])

db.session.add(cliente_info)
db.session.commit()

########

contato_info = Contatos(
                        tel1='11-testeErick',
                        tel2='11-testeErick-2',
                        email='testeErick@gmail.com'
                        )

endereco_info = Enderecos(
                        rua='Rua testeErick', numero=666,
                        bairro='Bairro testeErick', cidade='testeErick',
                        estado='AL', distancia=1000
                        )



cliente_info = Clientes('testeErick', 'H')

cliente_info.contato.append(contato_info)
cliente_info.endereco.append(endereco_info)

db.session.add(cliente_info)
db.session.commit()

# capeta ##########

cao_info = Peludos(
                    'belzebull', 'bull-terrier', 'longo',
                    datetime(1900, 1, 1),
                    datetime(2018, 10, 1), 'M', 'S'
                    )


cao_info2 = Peludos(
                    'baal', 'unk', 'curto',
                    datetime(1100, 2, 1),
                    datetime(2018, 10, 2), 'F', 'S'
                    )

cao_info3 = Peludos(
                    'lucy', 'unk', 'curto',
                    datetime(1100, 2, 1),
                    datetime(2018, 10, 2), 'F', 'S'
                    )


cao_info4 = Peludos(
                    'capiroto', 'unk', 'curto',
                    datetime(1100, 2, 1),
                    datetime(2018, 10, 2), 'M', 'N'
                    )


cliente_info = Clientes.query.filter_by(nome='capeta').first()
cliente_info
cliente_info.peludo.extend([cao_info, cao_info2, cao_info3, cao_info4])

db.session.add(cliente_info)
db.session.commit()



# mostra o nome do dono e do peludo
query = (
        db.session.query(
                            Clientes.nome.label("Cliente"),
                            Peludos.nome.label("dog"),
                            Peludos.breed.label('raça'),
                            Peludos.nascimento.label('idade'),
                            Enderecos.rua.label('Rua'),
                            Contatos.email.label('email')
                        )
        .join(Peludos, Enderecos, Contatos)
        )

# retorna resultado em tuplas
for item in query.all():
    print(item)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
