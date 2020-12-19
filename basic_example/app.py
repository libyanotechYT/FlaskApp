from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! or <h1>HELLO World</h1>"


if __name__ == '__main__':
    app.run()
