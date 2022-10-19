from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

