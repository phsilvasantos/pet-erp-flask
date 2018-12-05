"""Testing crud."""
from petshop import db
from petshop.modelos.models import *

email = 'erickfis@gmail.com'
senha = 'erickfis-EPR@blackStar'

gerente = Gerentes(email, senha)

db.session.add(gerente)

email = 'aline.medeiros03@gmail.com'
senha = 'aline-ERP@lpc'

gerente = Gerentes(email, senha)

gerente = Gerentes.query.first()

db.session.commit()
