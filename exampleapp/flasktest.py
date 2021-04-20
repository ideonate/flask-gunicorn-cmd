from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """<html><head></head><body>
    <h1>Hello World!</h1>
    <img src="./assets/ContainDS_logo_text.png" />
    </body>
    """

@app.route('/assets/<path:path>')
def send_img(path):
    return send_from_directory('assets', path)
