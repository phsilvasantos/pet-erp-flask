import babel
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from wtforms import (
                    StringField, SubmitField, SelectField, IntegerField,
                    DecimalField, DateField, SelectMultipleField
                    )
# import dash_core_components as dcc
# from datetime import datetime as dt

# from wtforms.fields.html5 import DateField


class Form_clientes(FlaskForm):
    """Form cliente."""

    nome = StringField('Nome Completo', validators=[DataRequired()])
    sexo = SelectField(
                        'Sexo', choices=[('M', 'Mulher'), ('H', 'Homem')],
                        validators=[DataRequired()]
                        )

    tel1 = StringField('tel1', validators=[DataRequired()])
    tel2 = StringField('tel2', validators=[DataRequired()])
    email = StringField('e-mail', validators=[DataRequired(), Email()])

    rua = StringField('Rua', validators=[DataRequired()])
    numero = IntegerField('Numero', validators=[DataRequired()])
    bairro = StringField('Bairo', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    estado = StringField('Estado', validators=[DataRequired()])
    distancia = DecimalField('Distancia', validators=[DataRequired()])

    submit = SubmitField('Adiciona cliente')


class Form_peludos(FlaskForm):
    """Form peludo."""

    cliente = SelectField(u'Dono do Peludo', choices=[], coerce=int)

    nome = StringField('Nome do peludo', validators=[DataRequired()])
    sexo = SelectField(
                        'Sexo', choices=[('M', 'Macho'), ('F', 'Fêmea')],
                        validators=[DataRequired()]
                        )
    breed = StringField('Raça', validators=[DataRequired()])
    pelagem = SelectField(
                        'Tipo de pelo',
                        choices=[('curto', 'Curto'), ('longo', 'Longo')],
                        validators=[DataRequired()]
                        )

    nascimento = DateField(
                            'Data de Nascimento', format='%d-%m-%Y',
                            validators=[DataRequired()]
                            )

    data_start = DateField('Date de início no pet', format='%d-%m-%Y',
                           validators=[DataRequired()])
    castrado = SelectField(
                            'Peludo foi castrado?',
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

    peludos = SelectMultipleField('Peludo(s)', choices=[], coerce=int)
    descricao = StringField('Descrição', validators=[DataRequired()])
    data_venda = DateField(
        'Data da venda', format='%d-%m-%Y', validators=[DataRequired()])


    valor_venda = DecimalField('Valor da venda',  # use_locale=True,
                               validators=[DataRequired()])
    valor_taxi = DecimalField('Valor do taxi dog',  # use_locale=True,
                              validators=[DataRequired()])
    n_banhos = IntegerField('Quantidade de banhos',
                            validators=[DataRequired()])
    tipo = SelectField('Avulso ou pacote',
                       choices=[
                                ('avulso', 'avulso'),
                                ('pacote', 'pacote')
                                ],
                       validators=[DataRequired()]
                       )

    pacote = StringField('Tipo de pacote', validators=[DataRequired()])
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

    data_pagto = DateField('Data de pagamento',
                           format='%d-%m-%Y', validators=[DataRequired()])
    valor_entrada = DecimalField(
        'Valor real de entrada',  # use_locale=True,
        validators=[DataRequired()])

    submit = SubmitField('Registrar venda')
