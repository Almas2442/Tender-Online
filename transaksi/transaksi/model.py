from transaksi import db

class Transaksi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_posting = db.Column(db.Integer)
    id_offering = db.Column(db.Integer)
    status = db.Column(db.String(50))