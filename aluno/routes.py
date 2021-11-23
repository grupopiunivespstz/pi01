from aluno import app
from flask import render_template, redirect, url_for, flash
from aluno.models import Aluno, ComposicaoFamiliar, Planejamento, Professor, Responsavel, Turma
from aluno.forms import Form_IncluirAluno, Form_IncluirComponenteFamiliar, Form_IncluirProfessor, Form_IncluirResponsavel, Form_IncluirTurma, Form_IncluirPlanejamento
from aluno import db


@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")


# Selecionar Tudo - Aluno
@app.route("/listagem_aluno", methods=["GET"])
def listagem_aluno():
    alunos = Aluno.query.all()
    return render_template("listagem_alunos.html", alunos=alunos)


# Selecionar Tudo - Composição Familiar
@app.route("/listagem_composicao_familiar", methods=["GET"])
def listagem_composicao_familiar():
    composicao_familiar = ComposicaoFamiliar.query.all()
    return render_template("listagem_composicao_familiar.html", composicao_familiar=composicao_familiar)


# Selecionar Tudo - Reponsável
@app.route("/listagem_responsavel", methods=["GET"])
def listagem_responsavel():
    responsaveis = Responsavel.query.all()
    return render_template("listagem_responsaveis.html", responsaveis=responsaveis)


# Selecionar Tudo - Turma
@app.route("/listagem_turma", methods=["GET"])
def listagem_turma():
    turmas = Turma.query.all()
    return render_template("listagem_turma.html", turmas=turmas)


# Selecionar Tudo - Professores
@app.route("/listagem_professor", methods=["GET"])
def listagem_professor():
    professores = Professor.query.all()
    return render_template("listagem_professor.html", professores=professores)


# Selecionar Tudo - Professores
@app.route("/listagem_planejamento", methods=["GET"])
def listagem_planejamento():
    planejamentos = Planejamento.query.all()
    return render_template("listagem_planejamento.html", planejamentos=planejamentos)


# incluir um novo aluno
@app.route("/novo_aluno", methods=['GET', 'POST'])
def novo_aluno():
    form = Form_IncluirAluno()
    if form.validate_on_submit():
        criar_aluno = Aluno(ra_aluno=form.ra_aluno.data,
                            nome=form.nome.data, sexo=form.sexo.data)
        db.session.add(criar_aluno)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            flash(f'Erro ao criar um aluno: {err_msg}')
    return render_template('novo_aluno.html', form=form)

# incluir um novo responsavel


@app.route("/novo_responsavel", methods=['GET', 'POST'])
def novo_responsavel():
    form = Form_IncluirResponsavel()
    if form.validate_on_submit():
        criar_responsavel = Responsavel(
            resp_nome=form.resp_nome.data, resp_fone_fixo=form.resp_fone_fixo.data, resp_fone_celular=form.resp_fone_celular.data, resp_whatsapp=form.resp_whatsapp.data)
        db.session.add(criar_responsavel)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            print(f'Erro ao criar um responsavel do aluno : {err_msg}')
    return render_template('novo_responsavel.html', form=form)


# incluir um novo componente familiar
@app.route("/novo_componente", methods=['GET', 'POST'])
def novo_componente():
    form = Form_IncluirComponenteFamiliar()
    if form.validate_on_submit():
        criar_componente = ComposicaoFamiliar(comp_id_aluno=form.comp_id_aluno.data,
                                              comp_nome=form.comp_nome.data, comp_escolaridade=form.comp_escolaridade.data, comp_parentesco=form.comp_parentesco.data)
        db.session.add(criar_componente)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            print(f'Erro ao criar um componente familiar : {err_msg}')
    return render_template('novo_componente.html', form=form)


# incluir uma nova turma
@app.route("/nova_turma", methods=['GET', 'POST'])
def nova_turma():
    form = Form_IncluirTurma()
    if form.validate_on_submit():
        criar_turma = Turma(turm_descricao=form.turm_descricao.data)
        db.session.add(criar_turma)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            print(f'Erro ao criar uma nova turma : {err_msg}')
    return render_template('novo_turma.html', form=form)


# incluir um novo professor
@app.route("/novo_professor", methods=['GET', 'POST'])
def novo_professor():
    form = Form_IncluirProfessor()
    if form.validate_on_submit():
        criar_professor = Professor(prof_nome=form.prof_nome.data, prof_funcao=form.prof_funcao.data,
                                    prof_telefone=form.prof_telefone.data, prof_celular=form.prof_celular.data)
        db.session.add(criar_professor)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            print(f'Erro ao criar um novo professor : {err_msg}')
    return render_template('novo_professor.html', form=form)


# incluir um novo planejamento
@app.route("/novo_planejamento", methods=['GET', 'POST'])
def novo_planejamento():
    form = Form_IncluirPlanejamento()
    if form.validate_on_submit():
        criar_planejamento = Planejamento(id_turma=form.id_turma.data, id_professor=form.id_professor.data, eixo=form.eixo.data, tema=form.tema.data, subtema=form.subtema.data, dta_inicio=form.dta_inicio.data, dta_final=form.dta_final.data,
                                          aulas_por_semana=form.aulas_por_semana.data, obj_geral=form.obj_geral.data, obj_especifico=form.obj_especifico.data, conhecer=form.conhecer.data, fazer=form.fazer.data, sentir=form.sentir.data)
        db.session.add(criar_planejamento)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            print(f'Erro ao criar um novo planejamento : {err_msg}')
    return render_template('novo_planejamento.html', form=form)


# rota inexistente
@app.route("/<string:rota_inexistente>")
def rota_inexistente(rota_inexistente):
    return f"<h1>{rota_inexistente} : Essa página não existe<h1>"
