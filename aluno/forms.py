from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.fields import choices
from wtforms.validators import Length


class Form_IncluirComponenteFamiliar(FlaskForm):
    comp_nome = StringField(label='Nome: ', validators=[
                            Length(min=5, max=120)])
    comp_escolaridade = SelectField(label='Escolaridade: ', validators=[
        Length(min=5, max=120)], choices=['ENSINO BÁSICO', 'ENSIMO MÉDIO', 'ENSINO TECNICO', 'ENSINO SUPERIOR'])
    comp_parentesco = SelectField(label='Parentesco: ', validators=[
        Length(min=2, max=120)], choices=['PAI', 'MÃE', 'AVÓ', 'AVÔ', 'TIA', 'TIO', 'PADRASTO', 'MADRASTA'])
    submit = SubmitField(label='Confirmar')


class Form_IncluirResponsavel(FlaskForm):
    resp_nome = StringField(label='Nome: ', validators=[
                            Length(min=5, max=120)])
    resp_fone_fixo = StringField(label='Telefone: ', validators=[
        Length(min=5, max=20)])
    resp_fone_celular = StringField(label='Whats App: ', validators=[
        Length(min=5, max=20)])
    resp_whatsapp = RadioField(label='Responde Whats App: ', choices=[
                               ('S', 'Sim'), ('N', 'Não')])
    submit = SubmitField(label='Confirmar')


class Form_IncluirAluno(FlaskForm):
    nome = StringField(label='Nome: ', validators=[Length(min=5, max=120)])
    ra_aluno = StringField(label='RA do aluno: ', validators=[
                           Length(min=5, max=30)])
    submit = SubmitField(label='Confirmar')
