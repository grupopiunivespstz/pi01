from aluno import db


class ComposicaoFamiliar(db.Model):
    __tablename__ = 'composicao_familiar'
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    comp_id_aluno = db.Column(db.Integer, db.ForeignKey("aluno.id"))
    comp_nome = db.Column(db.String(120))
    comp_idade = db.Column(db.Integer)
    comp_renda = db.Column(db.Float)
    comp_etnia = db.Column(db.String(1))
    comp_casa = db.Column(db.String(1))
    comp_tv = db.Column(db.String(1))
    comp_computador = db.Column(db.String(1))
    comp_dvd = db.Column(db.String(1))
    comp_microondas = db.Column(db.String(1))
    comp_carro = db.Column(db.String(1))
    comp_moto = db.Column(db.String(1))
    comp_celular = db.Column(db.String(1))
    comp_internet = db.Column(db.String(1))
    comp_empregada_domestica = db.Column(db.String(1))
    comp_assinante_jrn_rev = db.Column(db.String(1))
    comp_religiao = db.Column(db.String(1))
    comp_descreve_religiao = db.Column(db.String(60))
    comp_escolaridade = db.Column(db.String(120))
    comp_parentesco = db.Column(db.String(120))


class Responsavel(db.Model):
    __tablename__ = 'responsavel'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    resp_id_aluno = db.Column(db.Integer, db.ForeignKey("aluno.id"))
    resp_nome = db.Column(db.String(120))
    resp_nascimento = db.Column(db.Date)
    resp_cpf = db.Column(db.String(11))
    resp_rg = db.Column(db.String(20))
    resp_fone_fixo = db.Column(db.String(25))
    resp_fone_celular = db.Column(db.String(25))
    resp_whatsapp = db.Column(db.String(1))
    resp_local_trab = db.Column(db.String(120))
    resp_fone_trab = db.Column(db.String(25))
    resp_funcao_trab = db.Column(db.String(60))
    resp_tipo_resp = db.Column(db.String(1))
    resp_cidade = db.Column(db.String(120))
    resp_estado = db.Column(db.String(2))
    resp_logradouro = db.Column(db.String(120))
    resp_numero = db.Column(db.String(20))
    resp_complemento = db.Column(db.String(60))
    resp_bairro = db.Column(db.String(80))
    resp_cep = db.Column(db.String(8))
    resp_estado_civil = db.Column(db.String(120))


class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ra_aluno = db.Column(db.String(30), nullable=False)
    nome = db.Column(db.String(120))
    sexo = db.Column(db.String(1))
    responsavel = db.relationship(
        "Responsavel", backref="Responsavel", lazy=True)
    comp_familiar = db.relationship(
        "ComposicaoFamiliar", backref="ComposicaoFamiliar", lazy=True)
