from flask import Flask
import flask

app = Flask(__name__)
# configure where the static files are located
app.static_folder = ".."

@app.route('/login', methods=['POST'])
def login():
    # get user and password from request
    username = request.form["username"]
    password = request.form["password"]

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
