from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Email


class Form_cliente(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    nome = StringField('Nome Completo', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=[('M', 'Mulher'), ('H', 'Homem')],
                        validators=[DataRequired()])

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
