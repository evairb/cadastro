from flask import render_template, session, request, redirect, url_for, flash
from .forms import CadVisitanteForm
from .models import Visitante
from cadastro import app, db, bcrypt
import os

@app.route('/visitante/cadastrar', methods=['GET','POST'])
def cad_visitante():
    form = CadVisitanteForm(request.form)
    if request.method == 'POST':
        visitante = Visitante(name=form.name.data,n_mother=form.n_mother.data,cpf=form.cpf.data,email=form.email.data,andress=form.andress.data,
        code=form.code.data,country=form.country.data,state=form.state.data,city=form.city.data,fone=form.fone.data,fone2=form.fone2.data)
        db.session.add(visitante)
        db.session.commit()
        flash(f'Visitante {form.name.data} cadastrado com sucesso', 'success')
        return redirect(url_for('cad_visitante'))
        
    return render_template('visitante/visitante.html', form=form)


 
