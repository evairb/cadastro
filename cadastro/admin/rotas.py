from flask import render_template, session, request, redirect, url_for, flash
from .forms import LoginFormulario, RegistrationForm
from .models import Cargo, User
from cadastro import app, db, bcrypt
import os




@app.route('/admin')
def admin():
    if'cpf' not in session:
        flash('Realizar login no sistema', 'danger')
        return redirect(url_for('login'))
    return render_template ('admin/index.html', title='Pagina Administrativa')


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, cpf=form.cpf.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Obrigado por se registrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Registrar Usuario")




@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user= User.query.filter_by(cpf=form.cpf.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['cpf'] = form.cpf.data
            flash(f'Seja bem vindo','success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Nao foi possivel logar no sistema.') 
    return render_template('admin/login.html', title='Pagina Login', form=form)




@app.route('/addcargo', methods=['GET', 'POST'])
def addcargo():
    if request.method == "POST":
        getcargo = request.form.get('cargo')
        cargo = Cargo(cargo=getcargo)
        db.session.add(cargo)        
        flash(f'Cargo {getcargo} foi cadastrado com sucesso','success')
        db.session.commit()
        return redirect(url_for('addcargo'))
    return render_template('admin/addcargo.html',cargo='cargo')
  