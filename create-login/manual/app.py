from flask import Flask, render_template, request, make_response, session
from flask_restful import Api
import redis

app = Flask(__name__)
api = Api(app)

# Redis database
client = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

app.secret_key = "abc"  # harusnya disimpan di server production


# login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if client.get('username'):
        print("0")
        username = client.get('username')
        password = client.get('password')

        if username == 'admin' and password == '1':
            print(username)
            print("1")
            return '{} {}'.format("success",username)
        else:
            print("user pass salah")
            print("2")
            client.delete('username')
            client.delete('password')
            return "user atau password salah"
    else:
        if request.get_json():
            req = request.get_json()
            print(req)
            print("3")
            username = req['username']
            password = req['password']

            # save to redis
            print("set")
            client.set('username', username)
            client.set('password', password)

            if username == 'admin' and password == '1':
                print(username)
                print("4")
                return '{} {}'.format("success", username)
            else:
                print("user pass salah")
                print("5")
                # hapus redis user
                client.delete('username')
                client.delete('password')
                return render_template("login.html")
        return render_template("login.html")
    return "isi data"


# LOGOUT
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    client.delete('username')
    client.delete('password')
    print("success logout")
    return "logout"


# register
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html'), "hello"


# homes
@app.route("/home", methods=['GET', 'POST'])
def homes():
    if client.get('username'):
        print("coba")
        username = client.get('username')
        password = client.get('password')

        if username == 'admin' and password == '1':
            print(username)
            return render_template('homes.html')
        else:
            print("user pass salah")
            client.delete('username')
            client.delete('password')
            return render_template('login.html')
    return "login"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
