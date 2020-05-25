from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from transaksi.models import User

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/transaksi'

#mengaktifkan debug#
app.config['DEBUG'] = True

db = SQLAlchemy(app)

from transaksi import routes