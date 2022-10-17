from flask import Flask, render_template
from flask_bootstrap import Bootstrap

#Flask类接收一个参数__name__
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 