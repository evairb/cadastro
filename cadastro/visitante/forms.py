from wtforms import Form, BooleanField, StringField, validators, TextAreaField,IntegerField,SubmitField
from flask_wtf.file import FileAllowed, FileField, FileRequired

class CadVisitanteForm(Form):
    name = StringField('Nome:')
    n_mother = StringField('Nome Mae:', [validators.DataRequired()])
    cpf = IntegerField('CPF:',[validators.DataRequired()])
    email = StringField('Email:', [validators.DataRequired()])
    andress = TextAreaField('Endereco:', [validators.DataRequired()])
    code = IntegerField('Cep:', [validators.DataRequired()])
    country = StringField('Pais:', [validators.DataRequired()])
    state = StringField('Estado:', [validators.DataRequired()])
    city = StringField('Cidade:', [validators.DataRequired()])
    fone = IntegerField('Fone:', [validators.DataRequired()])
    fone2 = IntegerField('Contato:', [validators.DataRequired()])
    profile = FileField('Foto', validators=[FileAllowed(['jpg','png','git', 'jpeg'])])

    submit = SubmitField('Cadastrar')
