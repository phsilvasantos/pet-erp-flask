import babel
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms_components import (
                    StringField, SelectField, IntegerField,
                    DecimalField, DateField,
                    SelectMultipleField, DateRange
                    )
from wtforms.fields import SubmitField
from wtforms.validators import DataRequired, Email
# import dash_views_components as dcc


class Form_clientes(FlaskForm):
    """Form cliente."""

    nome = StringField('Nome Completo', validators=[DataRequired()])
    sexo = SelectField(
                        'Sexo', choices=[('M', 'Mulher'), ('H', 'Homem')],
                        validators=[DataRequired()]
                        )

    tel1 = StringField('Tel.1', validators=[DataRequired()])
    tel2 = StringField('Tel.2', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])

    rua = StringField('Rua', validators=[DataRequired()])
    numero = IntegerField('Número', validators=[DataRequired()])
    bairro = StringField('Bairo', validators=[DataRequired()])
    cidade = StringField('Cidade', default='Santo André', validators=[DataRequired()])
    estado = StringField('Estado', default='SP', validators=[DataRequired()])
    distancia = DecimalField('Distância', default=5, validators=[DataRequired()])

    submit = SubmitField('Adiciona cliente')


class Form_peludos(FlaskForm):
    """Form peludo."""

    cliente = SelectField(u'Dono do Peludo', choices=[], coerce=int)

    nome = StringField('Nome do peludo', validators=[DataRequired()])
    sexo = SelectField(
                        'Sexo', choices=[('M', 'Macho'), ('F', 'Fêmea')],
                        validators=[DataRequired()]
                        )
    breed = StringField('Raça', default='Shitzu', validators=[DataRequired()])
    pelagem = SelectField(
                        'Tipo de pelo',
                        choices=[('curto', 'Curto'), ('longo', 'Longo')],
                        validators=[DataRequired()]
                        )

    nascimento = DateField(
                            'Data de Nascimento',
                            validators=[DataRequired()]
                            )

    data_start = DateField('Date de início no pet', # format='%d-%m-%Y',
                           validators=[DataRequired()])
    castrado = SelectField(
                            'É castrado?',
                            choices=[('S', 'Sim'), ('N', 'Não')],
                            validators=[DataRequired()]
                            )

    submit = SubmitField('Adiciona peludo')


class Form_vendas_intro(FlaskForm):
    """Form venda_intro."""

    cliente = SelectField(u'Dono do peludo', choices=[], coerce=int)
    submit = SubmitField('Continuar venda')


class Form_vendas(FlaskForm):
    """Form venda."""

    # cliente = SelectField(u'Dono do peludo', choices=[], coerce=int)

    peludos = SelectMultipleField('Peludo(s)', choices=[], coerce=int)
    descricao = StringField('Descrição', validators=[DataRequired()])

    valor_servicos = DecimalField('Valor de serviços',  # use_locale=True,
                               validators=[DataRequired()])
    valor_taxi = DecimalField('Valor do taxi dog', default=0,  # use_locale=True,
                              validators=[DataRequired()])
    n_banhos = IntegerField('Quantidade de banhos', default=1,
                            validators=[DataRequired()])
    tipo = SelectField('Avulso ou pacote',
                       choices=[
                                ('avulso', 'avulso'),
                                ('pacote', 'pacote')
                                ],
                       validators=[DataRequired()]
                       )

    pacote = StringField('Tipo de pacote', default="puka",
                         validators=[DataRequired()])

    forma_pagto = SelectField('Forma de pagamento',
                              choices=[
                                        ('cash', 'cash'),
                                        ('debito', 'debito'),
                                        ('credito', 'credito'),
                                        ('cheque', 'cheque'),
                                        ('pendente', 'pendente')
                                        ],
                              validators=[DataRequired()]
                              )

    data_pagto = DateField('Data de pagamento', default=datetime.today(),
                          validators=[DataRequired()])

    valor_entrada = DecimalField(
        'Valor real de entrada',  # use_locale=True,
        validators=[DataRequired()])

    submit = SubmitField('Registrar venda')
