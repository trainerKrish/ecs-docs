from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/new")
def hello_world():
    return "<p>Hello, Universe!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!!!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
