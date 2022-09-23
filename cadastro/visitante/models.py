from cadastro import db

from datetime import datetime
from tzlocal import get_localzone
from pytz import timezone

dt = datetime.now()
fuso = timezone('America/Sao_Paulo')
data = dt.astimezone(fuso)
dt_sp = data.strftime('%Y-%m-%d %H:%M:%S')

print(dt_sp)

class Visitante(db.Model):
    __tablename__='Visitante'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False)
    n_mother = db.Column(db.String(60), unique=False)
    cpf = db.Column(db.Integer, unique=True)
    andress = db.Column(db.String(60),unique=False)
    email = db.Column(db.String(60), unique=True)
    code = db.Column(db.String(60), unique=False)
    country = db.Column(db.String(60), unique=False)
    state = db.Column(db.String(60), unique=False)
    city = db.Column(db.String(60), unique=False)
    fone = db.Column(db.String(60), unique=False)
    fone2 = db.Column(db.String(60), unique=False)
    profile = db.Column(db.String(60), unique=False)
    date =db.Column(db.DateTime, default=dt_sp)

    def __repr__(self):
        return '<Visitante %r>' % self.name

    

db.create_all()