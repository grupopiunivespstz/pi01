
from flask import Flask, render_template
from wtforms import StringField, SelectField, RadioField, SubmitField, TextAreaField
from flask_wtf import Form, FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import IntegerField
from wtforms_sqlalchemy.fields import QuerySelectField
from .models import Aluno, Turma, Professor, Planejamento
from wtforms.validators import Length


class Form_IncluirProfessor(FlaskForm):
    prof_nome = StringField(label='Nome do Professor: ', validators=[
        Length(min=5, max=120)])
    prof_funcao = SelectField(label='Função: ', validators=[
        Length(min=5, max=60)], choices=['Professor', 'Monitor'])
    prof_telefone = StringField(label='Núm. de Telefone: ', validators=[
        Length(min=5, max=20)])
    prof_celular = StringField(label='Núm. de Celular: ', validators=[
        Length(min=5, max=20)])
    submit = SubmitField(label='Confirmar')


class Form_IncluirTurma(FlaskForm):
    turm_descricao = StringField(label='Descrição: ', validators=[
        Length(min=5, max=120)])
    submit = SubmitField(label='Confirmar')


class Form_IncluirComponenteFamiliar(FlaskForm):
    comp_id_aluno = QuerySelectField(
        'Escolha o aluno: ', query_factory=lambda: Aluno.query, get_label='nome')
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
    resp_id_aluno = QuerySelectField(
        u'Escolha o aluno: ',
        query_factory=lambda: Aluno.query, get_label='nome')                            
    submit = SubmitField(label='Confirmar')


class Form_IncluirAluno(FlaskForm):
    nome = StringField(label='Nome: ', validators=[Length(min=5, max=120)])
    ra_aluno = StringField(label='RA do aluno: ', validators=[
                           Length(min=5, max=30)])
    sexo = RadioField(label='Sexo: ', choices=[
                      ('M', 'Masculino'), ('F', 'Feminino')])
    turma = QuerySelectField(
        u'Escolha a turma: ',
        query_factory=lambda: Turma.query, get_label='turm_descricao')
    submit = SubmitField(label='Confirmar')


class Form_IncluirPlanejamento(FlaskForm):
    id_turma = QuerySelectField(
        'Escolha a turma: ', query_factory=lambda: Turma.query, get_label='turm_descricao')
    id_professor = QuerySelectField(
        'Escolha o professor: ', query_factory=lambda: Professor.query, get_label='prof_nome')
    eixo = StringField(label='Eixo: ', validators=[
        Length(min=5, max=50)])
    tema = StringField(label='Tema: ', validators=[
        Length(min=5, max=50)])
    subtema = StringField(label='Sub-Tema: ', validators=[
        Length(min=5, max=50)])
    dta_inicio = DateField(label='Data de Início: ')
    dta_final = DateField(label='Data de Fim: ')
    aulas_por_semana = IntegerField(label='Aulas por Semana: ')
    obj_geral = TextAreaField(label='Objetivo Geral: ', validators=[
        Length(min=5, max=1024)])
    obj_especifico = TextAreaField(label='Objetivo Específico: ', validators=[
        Length(min=5, max=1024)])
    conhecer = TextAreaField(label='Conhecer: ', validators=[
        Length(min=5, max=1024)])
    fazer = TextAreaField(label='Fazer: ', validators=[
        Length(min=5, max=1024)])
    sentir = TextAreaField(label='Sentir: ', validators=[
        Length(min=5, max=1024)])
    submit = SubmitField(label='Confirmar')
