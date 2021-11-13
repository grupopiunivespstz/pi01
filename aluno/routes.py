from types import resolve_bases
from aluno import app
from flask import render_template, redirect, url_for
from aluno.models import Aluno, ComposicaoFamiliar, Responsavel
from aluno.forms import Form_IncluirAluno, Form_IncluirComponenteFamiliar, Form_IncluirResponsavel
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


# incluir um novo aluno
@app.route("/novo_aluno", methods=['GET', 'POST'])
def novo_aluno():
    form = Form_IncluirAluno()
    if form.validate_on_submit():
        criar_aluno = Aluno(ra_aluno=form.ra_aluno.data, nome=form.nome.data)
        db.session.add(criar_aluno)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            print(f'Erro ao criar um aluno: {err_msg}')
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
        criar_componente = ComposicaoFamiliar(
            comp_nome=form.comp_nome.data, comp_escolaridade=form.comp_escolaridade.data, comp_parentesco=form.comp_parentesco.data)
        db.session.add(criar_componente)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.erros.values():
            print(f'Erro ao criar um componente familiar : {err_msg}')
    return render_template('novo_componente.html', form=form)


# rota inexistente
@app.route("/<string:rota_inexistente>")
def rota_inexistente(rota_inexistente):
    return f"<h1>{rota_inexistente} : Essa página não existe<h1>"
