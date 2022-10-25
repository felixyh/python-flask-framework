from flask import Flask, render_template
from sqlhelper import db

app = Flask(__name__, template_folder='./')


@app.route('/index')
def index():
    result = db.fetchall('select * from albums')
    return render_template('index.html', result=result)

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
