from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    """Return simple "Hello" Greeting."""

    html = "<html><body><h1>Hello World! I am coming alive!</h1></body></html>"
    return html

@app.route('/goodbye')
def say_goodbye():
    """Return simple "Goodbye" Greeting."""

    html = "<html><body><h1>Goodbye World! I am leaving for another route for now!</h1></body></html>"
    return html