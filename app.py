from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return '<a href=' + url_for("hello", name="no name") + '>let yourself be welcomed</a>'


@app.route("/hello/<string:name>")
def hello(name):
    return "Hello " + name

@app.route("/hello_num/<int:name>")
def hello_int(name):
    return "Hello " + str(name)

@app.route("/hello_num/<float:name>")
def hello_float(name):
    return "Hello " + str(name)

if __name__ == "__main__":
    app.run(port=1337, debug=True)
