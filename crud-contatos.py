"""Testing crud."""
from pet import db
from pet.models import cliente, cachorro, contato, endereco, venda
from datetime import datetime
import pandas as pd
# db.metadata.clear()
# db.create_all()


cliente.query.all()
contato_aline = contato(tel1='11-95276-2922', tel2='11-98183-6620',
                    email='aline.medeiros03@gmail.com')


aline = cliente.query.filter(cliente.nome.ilike('aline')).first()
aline.contato.append(contato_aline)

endereco_aline = endereco(
            rua='Rua Irlanda', numero=554,
            bairro='Capuava', cidade='Santo André',
            estado='SP', distancia=0)


aline.endereco.append(endereco_aline)

db.session.add(aline)
db.session.commit()

### marcelo
marcelo = cliente.query.filter(cliente.nome.ilike('marcelo')).first()

adress = endereco(
            rua='Rua teste marcelo', numero=000,
            bairro='bairo testo marcelo', cidade='Calgary',
            estado='AL', distancia=1000)

contact = contato(tel1='99-marcelo', tel2='88-marcelo',
                email='marcelo@gmail.com')


marcelo.endereco.append(adress)
marcelo.contato.append(contact)

### amanda
amanda = cliente.query.filter(cliente.nome.ilike('amanda')).first()

adress = endereco(
            rua='Rua teste amanda', numero=000,
            bairro='bairo testo amanda', cidade='Santo André',
            estado='SP', distancia=2)

contact = contato(tel1='99-amanda', tel2='88-amanda',
                email='amanda@gmail.com')


amanda.endereco.append(adress)
amanda.contato.append(contact)

## commit

db.session.add_all([amanda, marcelo])
db.session.commit()

# mostra o nome do dono e do cachorro
query = db.session.query(
    cliente.nome.label("cliente"),
    cachorro.nome.label("dog"),
    cachorro.breed.label('raça'),
    cachorro.nascimento.label('idade'),
    endereco.rua.label('Rua'),
    contato.email.label('email')
    ).join(cachorro, endereco, contato)

# retorna resultado em tuplas
for item in query.all():
    print(item)


# coloca em df
df = pd.read_sql(query.statement, db.session.bind)
df
