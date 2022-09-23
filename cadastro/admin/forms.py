from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField
from flask_wtf.file import FileAllowed, FileField, FileRequired

class RegistrationForm(Form):
    name = StringField('Nome Completo:', [validators.Length(min=4, max=25)])
    cpf = StringField('CPF', [validators.Length(min=11, max=11)])
    cargo = StringField('Cargo', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senhas diferentes')
    ])
    confirm = PasswordField('Repita a senha')


class LoginFormulario(Form):
    cpf = StringField('CPF', [validators.Length(min=11, max=11)])
    password = PasswordField('Senha', [validators.DataRequired()])

class Addcargo(Form):
    name = StringField('Nome:', [validators.DataRequired])
    