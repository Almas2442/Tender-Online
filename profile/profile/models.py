from profile import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    almas = db.Column(db.String(50))