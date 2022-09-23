from cadastro import db



class Cargo(db.Model):
    __tablename__='Cargo'
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(80), unique=True)


class User(db.Model):
    __tablename__='User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    cpf = db.Column(db.Integer, unique=True)
    cargo = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(180), unique=False)

    #photo = db.Column(db.String(180), unique=False,default='photo.jpg')

db.create_all()