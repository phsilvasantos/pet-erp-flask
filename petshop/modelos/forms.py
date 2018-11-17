import babel
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms_components import (
                    StringField, SelectField, IntegerField,
                    DecimalField, DateField,
                    SelectMultipleField, DateRange
                    )
from wtforms.fields import SubmitField, FloatField
from wtforms.validators import DataRequired, Email


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
    cidade = StringField('Cidade', default='Santo André',
                         validators=[DataRequired()])
    estado = StringField('Estado', default='SP', validators=[DataRequired()])
    distancia = DecimalField('Distância', default=5,
                             validators=[DataRequired()])

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

    data_start = DateField('Date de início no pet',  # format='%d-%m-%Y',
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


class Form_vendas_bt(FlaskForm):
    """Form venda bt."""

    # cliente = SelectField(u'Dono do peludo', choices=[], coerce=int)
    descricao = StringField('Descrição', validators=[DataRequired()])
    data_venda = DateField('Data da venda', default=datetime.today(),
                           validators=[DataRequired()])

    valor_servicos = DecimalField('Valor de serviços',
                                  validators=[DataRequired()]
                                  )

    valor_taxi = DecimalField('Valor do taxi dog', default=0,
                              # validators=[DataRequired()]
                              )

    peludos = SelectMultipleField('Peludo(s)', choices=[], coerce=int,
                                  validators=[DataRequired()]
                                  )

    data_pbanho = DateField('Data do primeiro banho', default=datetime.today(),
                            validators=[DataRequired()]
                            )

    n_banhos = IntegerField('Quantidade de banhos', default=1,
                            validators=[DataRequired()]
                            )

    tipo_banho = SelectField('Avulso ou pacote',
                             choices=[
                                ('avulso', 'avulso'),
                                ('pacote', 'pacote')
                                ],
                             validators=[DataRequired()]
                             )

    pacote = StringField('Tipo de pacote', default="puka",
                         validators=[DataRequired()])

    submit = SubmitField('Registrar venda')


class Form_vendas_hosp(FlaskForm):
    """Form venda hospedagem."""

    # cliente = SelectField(u'Dono do peludo', choices=[], coerce=int)
    descricao = StringField('Descrição', validators=[DataRequired()])

    data_venda = DateField('Data da venda', default=datetime.today(),
                           validators=[DataRequired()]
                           )

    valor_servicos = DecimalField('Valor de serviços adicionais',
                                  validators=[DataRequired()]
                                  )

    valor_taxi = DecimalField('Valor do taxi dog', default=0,
                              validators=[DataRequired()]
                              )

    peludos = SelectMultipleField('Peludo(s)', choices=[], coerce=int)

    n_banhos = IntegerField('Quantidade de banhos', default=0,
                            validators=[DataRequired()]
                            )

    data_entrada = DateField('Data de entrada na hospedagem',
                             default=datetime.today(),
                             validators=[DataRequired()]
                             )

    data_saida = DateField('Data de saída da hospedagem',
                           default=datetime.today(),
                           validators=[DataRequired()]
                           )

    valor_diarias = DecimalField('Valor total de diárias', default=0,
                                 validators=[DataRequired()]
                                 )

    submit = SubmitField('Registrar venda')


class Form_vendas_cursos(FlaskForm):
    """Form venda cursos."""

    # cliente = SelectField(u'Dono do peludo', choices=[], coerce=int)
    descricao = StringField('Descrição', validators=[DataRequired()])

    data_venda = DateField('Data da venda', default=datetime.today(),
                           validators=[DataRequired()])

    valor_servicos = DecimalField('Valor de serviços',
                                  validators=[DataRequired()])

    data_entrada = DateField('Data de início do curso',
                             default=datetime.today(),
                             validators=[DataRequired()]
                             )

    data_saida = DateField('Data de término do curso',
                           default=datetime.today(),
                           validators=[DataRequired()]
                           )

    custo_prod = DecimalField('Custos do curso', default=0,
                              validators=[DataRequired()]
                              )

    submit = SubmitField('Registrar venda')


class Form_vendas_prod(FlaskForm):
    """Form venda produtos."""

    # cliente = SelectField(u'Dono do peludo', choices=[], coerce=int)
    descricao = StringField('Descrição', validators=[DataRequired()])
    data_venda = DateField('Data da venda', default=datetime.today(),
                           validators=[DataRequired()])

    valor_prod = DecimalField('Valor dos produtos', default=0,
                              validators=[DataRequired()]
                              )

    custo_prod = DecimalField('Custo dos produtos', default=0,
                              validators=[DataRequired()]
                              )

    submit = SubmitField('Registrar venda')


class Form_pagamentos(FlaskForm):
    """Form pagamentos."""

    forma_pagto = SelectField('Forma de pagamento',
                              choices=[
                                        ('cash', 'cash'),
                                        ('debito', 'debito'),
                                        ('transf', 'transferencia'),
                                        ('credito', 'credito'),
                                        ('cheque', 'cheque'),
                                        ('pendente', 'pendente'),
                                        ('cortesia', 'cortesia')
                                        ],
                              validators=[DataRequired()]
                              )

    data = DateField('Data de pagamento', default=datetime.today(),
                           validators=[DataRequired()])

    valor = FloatField(
                                'Valor pago',
                                validators=[DataRequired()]
                                )

    valor_entrada = FloatField(
                                'Valor real de entrada',
                                validators=[DataRequired()]
                                )

    submit = SubmitField('Registrar pagamento')