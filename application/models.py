from application import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))