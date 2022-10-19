from flask import Flask

from flask_sqlalchemy import flask_sqlalchemy
import config


app = Flask(__name__)
db = flask_sqlalchemy(app)

app.config.from_object(config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
