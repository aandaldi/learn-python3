from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import redis

app = Flask(__name__)
url = 'mysql+pymysql://local:local@localhost/users_database'
app.config['SQLALCHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)

cache = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.String(80))
    email_address = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String(80))

    def __init__(self, created_at, created_by, email_address, first_name, last_name, updated_at, updated_by):
        self.created_at = created_at
        self.created_by= created_by
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.updated_at = updated_at
        self.updated_by = updated_by

    def json(self):
        return {'created_by':self.created_by, 'email_address':self.email_address, 'first_name':self.first_name,
                'last_name':self.last_name, 'updated_by':self.updated_by}

def getUsers():
    users = cache.get('users')
    if not users:
        print("belum ada di cache")
        users = User.query.first()
        users = users.json()
        print(users)
        print("belum ada di cache")
        cache.set('users', users)
        print("save to cache")
        print(cache.get('users'))
        return cache.get('users')
    else:
        print("ada di cache")
        users = cache.get('users')
        print(users)
        return users

def getListUsers():
    listusers = cache.lrange('listusers', 0, 10)
    if not listusers:
        print("belum ada di redis")
        list = User.query.all()
        for user in list:
            pengguna = user.json()
            cache.lpush('listusers', pengguna)
        print(cache.lrange('listusers', 0, 10))
    else:
        print("ada di cache")
        print(listusers)
        print(type(listusers))
        for x in listusers:
            print(x)
        return jsonify(listusers)




# improvement: views/routing should stay in a different file
@app.route('/')
def hello_world():
    return getUsers()

@app.route('/listusers')
def listusers():
    return getListUsers()
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')