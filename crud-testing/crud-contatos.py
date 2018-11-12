"""Testing crud."""
from pet import db
from pet.models import Cliente, Peludo, Contato, Endereco, Venda
from datetime import datetime
import pandas as pd
# db.metadata.clear()
# db.create_all()


Cliente.query.all()
contato_aline = Contato(tel1='11-95276-2922', tel2='11-98183-6620',
                    email='aline.medeiros03@gmail.com')


aline = Cliente.query.filter(Cliente.nome.ilike('aline')).first()
aline.contato.append(contato_aline)

endereco_aline = Endereco(
            rua='Rua Irlanda', numero=554,
            bairro='Capuava', cidade='Santo André',
            estado='SP', distancia=0)


aline.endereco.append(endereco_aline)

db.session.add(aline)
db.session.commit()

### marcelo
marcelo = Cliente.query.filter(Cliente.nome.ilike('marcelo')).first()

address = Endereco(
            rua='Rua teste marcelo', numero=000,
            bairro='bairo testo marcelo', cidade='Calgary',
            estado='AL', distancia=1000)

contact = Contato(tel1='99-marcelo', tel2='88-marcelo',
                email='marcelo@gmail.com')


marcelo.endereco.append(address)
marcelo.contato.append(contact)

### amanda
amanda = Cliente.query.filter(Cliente.nome.ilike('amanda')).first()

adress = Endereco(
            rua='Rua teste amanda', numero=000,
            bairro='bairo testo amanda', cidade='Santo André',
            estado='SP', distancia=2)

contact = Contato(tel1='99-amanda', tel2='88-amanda',
                email='amanda@gmail.com')


amanda.endereco.append(adress)
amanda.contato.append(contact)

## commit

db.session.add_all([amanda, marcelo])
db.session.commit()

# mostra o nome do dono e do peludo
query = db.session.query(
    Cliente.nome.label("Cliente"),
    Peludo.nome.label("dog"),
    Peludo.breed.label('raça'),
    Peludo.nascimento.label('idade'),
    Endereco.rua.label('Rua'),
    Contato.email.label('email')
    ).join(Peludo, Endereco, Contato)

# retorna resultado em tuplas
for item in query.all():
    print(item)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
