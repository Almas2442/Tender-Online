from posting import db

class Posting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_product = db.Column(db.String(50))
    brand = db.Column(db.String(50))
    description = db.Column(db.String(50))
    picture = db.Column(db.String(50))
    id_profile_buyer = db.Column(db.Integer)
    tgl_buat = db.Column(db.String(50))