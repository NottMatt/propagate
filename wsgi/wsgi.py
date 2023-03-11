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


@app.route('/is-logged-in', methods=['GET'])
def is_logged_in():
    if 'user_id' in flask.session.keys():
        return {'response': True}
    else:
        return {'response': False}


@app.route('/logout', methods=['GET'])
def logout():
    flask.session.pop('username', None)
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


@app.route('/profile', methods=['GET'])
def profile():
    return app.send_static_file('html/profile.html')


@app.route("/")
def index_route():
    return app.send_static_file("index.html")


@app.route('/library', methods=['GET'])
def library():
    if 'user_id' not in flask.session.keys():
        return flask.redirect(flask.url_for("login"))
    with get_db_connection() as conn, conn.cursor() as cur:
        cur.execute(f'''
        select * from components left join saved_components on component_id =
        components.id where creator_id = {flask.session["user_id"]} or user_id
        = {flask.session["user_id"]} ;
        ''')
        library = cur.fetchall()
        return library


# Handle Components
@app.route('/component', methods=['GET', 'POST'])
def component():
    # Bail out if this user is not logged in
    if 'user_id' not in flask.session:
        return flask.redirect(flask.url_for("login"))

    if flask.request.method == 'POST':
        creator_id = flask.session['user_id']
        component_name = request.form['component_name']
        description = request.form['description']
        content = request.form['content']

        # Needs testing
        with get_db_connection() as conn, conn.cursor() as cur:
            if 'preceded_by' in request.form.keys():
                preceded_by = request.form['preceded_by']
                cur.execute('''
                insert into components (creator_id, component_name,
                description, content, preceded_by) values (%(creator_id)i,
                %(name)s, %(description)s, %(content)s, %(preceded_by)i)
                ''', 
                {'creator_id': creator_id, 'name': component_name,
                    'description': description, 'content': content,
                    'preceded_by': preceded_by})
            else:
                cur.execute('''
                insert into components (creator_id, component_name,
                description, content) values (%(creator_id)i, %(name)s,
                %(description)s, %(content)s)
                ''', 
                {'creator_id': creator_id, 'name': component_name,
                    'description': description, 'content': content})
    else:
        component_id = request.args.get('id')
        with get_db_connection() as conn, conn.cursor() as cur:
            cur.execute("select * from components where id = '%(id)' ;", {'id': component_id})
            component = cur.fetchone()
            if component is None:
                print(f'Error getting component from id', file=sys.stderr)
            else:
                print(f'We haven\'t handled this case yet, oops', file=sys.stderr)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='propagate',
                            user='flask',
                            password='password')
    return conn

def get_username_from_id(id: str) -> str:
    with get_db_connection() as conn, conn.cursor() as cur:
        cur.execute("select username from users where id = '%(user_id)' ;", {'user_id': id})
        user = cur.fetchone()
        if user is None:
            print(f'Error getting username from id', file=sys.stderr)
            return None
    return user
