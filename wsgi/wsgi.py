import flask
from flask import Flask, request
import psycopg2
import sys
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

# configure where the static files are located
app.static_folder = ".."

@app.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'POST':
        # get user and password from request
        username = request.form["username"]
        password = request.form["password"]

        with get_db_connection() as conn, conn.cursor() as cur:
            cur.execute('select * from users where username = %(username)s ;', {'username': username})
            user_id = cur.fetchall()

            if len(user_id) == 0:
                print('Login failed: {username}', file=sys.stderr)
                return app.send_static_file("html/login-failure.html")
            else:
                print(f'Login successful: {username}:{user_id[0][0]}', file=sys.stderr)
                flask.session['user_id'] = user_id[0][0]
                flask.session['username'] = username
                return flask.redirect(flask.url_for("index_route"))
    else:
        return app.send_static_file('html/login.html');


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return flask.redirect(flask.url_for("index_route"))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if flask.request.method == 'POST':
        # get user and password from request
        username = request.form["username"]
        password_1 = request.form["password_1"]
        password_2 = request.form["password_2"]

        with get_db_connection() as conn, conn.cursor() as cur:
            cur.execute('select * from users where username = %(username)s ;',
                    {'username': username})
            users = cur.fetchall()
            print(f'User: {users}', file=sys.stderr)
            if len(users) == 0:
                cur.execute('insert into users (username, password) values (%(username)s, %(password)s)', 
                        {'username': username, 'password': password_1})
                return flask.redirect(flask.url_for("index_route"))
            else:
                return flask.redirect(flask.url_for("registration_failed"))
    else:
        return app.send_static_file('html/create-user.html')

@app.route('/registration_failed', methods=['GET'])
def registration_failed():
    return app.send_static_file('html/registration-failure.html')


# serve the static files
@app.route("/<path:path>", methods=["GET"])
def serve_static_files(path):
    try:
        if path.startswith("html/"):
            return app.send_static_file(path)
        elif path.startswith("svg/"):
            return app.send_static_file(path)
        elif path.startswith("style/"):
            return app.send_static_file(path)
        elif path.startswith("js/"):
            return app.send_static_file(path)
        elif path == "style.css":
            return app.send_static_file(path)
        elif path == "index.html":
            return app.send_static_file(path)
        else:
            print(f"Error: {path} is not a valid path", file=sys.stderr)
            return flask.redirect(flask.url_for("index_route"))
    except:
        # redirect and log failed request
        return flask.redirect(flask.url_for("index_route"))

@app.route('/gate-editor', methods=['GET'])
def gate_editor():
    return app.send_static_file('html/gate-editor.html')

@app.route("/")
def index_route():
    return app.send_static_file("index.html")

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='propagate',
                            user='flask',
                            password='password')
    return conn
