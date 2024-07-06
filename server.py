import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<path:filename>")
def serve_static(filename):
	return flask.send_from_directory("templates",filename)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)