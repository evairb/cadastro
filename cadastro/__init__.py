from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
#app.config['SQALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres@localhost/cadastro'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/cadastro'
app.config['SECRET_KEY']='asfasfasf'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from cadastro.admin import rotas
from cadastro.visitante import rotas