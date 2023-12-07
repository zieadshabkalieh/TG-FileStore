from flask import Flask
from werkzeug.urls import quote
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'GreyMatters'


if __name__ == "__main__":
    app.run()
