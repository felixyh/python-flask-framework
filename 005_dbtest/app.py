from flask import Flask

from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

