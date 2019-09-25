from application import db

class User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class News(db.Model):
    __tablename__ = 'news'
    __bind_key__ = 'news'
    __table_args__ = {"schema": "exclude_from_migrations"}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

