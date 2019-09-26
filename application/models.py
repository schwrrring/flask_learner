from application import db

class User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = None
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class News(db.Model):
    __tablename__ = 'news'
    __bind_key__ = None
    # __table_args__ = {"schema": "exclude_from_migrations"}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    nix = db.Column(db.String(128))

class Meldung(db.Model):
    __tablename__ = 'meldungen'
    __bind_key__ = 'meldungen'
    id = db.Column(db.Integer, primary_key=True)
    hidden_name = db.Column(db.String(128))
    name = db.Column(db.String(128))
