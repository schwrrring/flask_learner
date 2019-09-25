from application import db
from application.models import User
from flask import current_app as app

@app.route("/<username>", methods=['GET', 'POST', 'PUT'])
def add_user(username):
    new_user = User(name=username)
    db.session.add(new_user)
    db.session.commit()
    return 'hello'

@app.route("/user/<username>", methods=['GET', 'POST', 'PUT'])
def get_user(username):
    user_id = db.session.query(User).filter(User.name == username).first()
    print(user_id.id, '//////////')
    return str(user_id.id)