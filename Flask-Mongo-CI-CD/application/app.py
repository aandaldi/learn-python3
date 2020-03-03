import unittest
import json
from config import config_by_name
from flask import Flask, jsonify, request
from flask_script import Manager

from flask_pymongo import PyMongo

config_name = 'dev'

app = Flask(__name__)
manager = Manager(app)
app.config.from_object(config_by_name[config_name])
mongo = PyMongo(app)
user_col = mongo.db.user
user_col.drop()


@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)


@manager.command
def test():
    config_name = 'test'
    app.config.from_object(config_by_name[config_name])

    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


# ENDPOINT

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello, welcome to my app'
    }), 200


@app.route('/insert/', methods=['GET', 'POST'])
def insertUser():
    name = request.args['name']
    npk = request.args['npk']
    # print(name,npk)
    new_user = dict(
        name=name,
        npk=npk
    )
    user_col.insert_one(new_user)
    list_user = []
    for x in user_col.find():
        x['_id'] = str(x['_id'])
        list_user.append(x)
    # print(list_user)
    return jsonify(user=list_user), 201


@app.route('/list', methods=['GET', 'POST'])
def listUser():
    list_user = []
    for user in user_col.find():
        user['_id'] = str(user['_id'])
        list_user.append(user)
    return jsonify(users=list_user)

@app.route('/remove/', methods=['GET','POST'])
def removeUser():
    npk=request.args['npk']
    user = {"npk": npk}
    print(user)
    user_col.delete_one(user)

    return "list"

@app.route('/update/', methods=['GET', 'POST'])
def updateUser():
    name = request.args['name']
    new_name = request.args['new_name']
    query = {"name": name}
    update_query = {"$set":{"name":new_name}}

    user_col.update_one(query,update_query)
    list_user = []
    for x in user_col.find():
        x['_id'] = str(x['_id'])
        list_user.append(x)
    print(list_user)
    return jsonify(user=list_user)

if __name__ == '__main__':
    manager.run()
