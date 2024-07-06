import flask

app = flask.Flask(__name__)

@app.route("/<path:filename>")
def serve_static(filename):
	return flask.send_from_directory("deploy",filename)
	
@app.route("/")
def index():
	return flask.send_from_directory("deploy","main.html")