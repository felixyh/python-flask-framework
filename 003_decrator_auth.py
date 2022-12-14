from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from random import randint

from flask import session

from functools import wraps



app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

DATA_DICT = {
    1: {'name': 'Feix', 'age': 40},
    2: {'name': 'Daniel', 'age': 38}
}

def auth(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if 'username' in session:
            logsuccessmsg =  f'Logged in as {session["username"]}'
            return func(*args, **kwargs)
        flash('You are not logged in')
        return redirect(url_for('login'))
    return inner


@app.route('/index', endpoint='idx')
@auth
def index():
    data_dict = DATA_DICT
    return render_template('index.html', data_dict=data_dict)


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template('login.html')

    user = request.form.get('user')
    password = request.form.get('password')
    if user == 'felix' and password == 'novirus':
        # add session, 'username' is the key defined, could be any , such as 'xxx'
        session['username'] = request.form.get('user')
        return redirect('/index')
    
    error = '用户名或者密码错误'
    warning = '警告信息！'
    return render_template('login.html', error=error, warning=warning)

@app.route('/logout')
@auth
def logout():
    # remove the suername from the session if it's there
    session.pop('username', None)
    return redirect(url_for('idx'))


@app.route('/add', methods=['GET', 'POST'])
@auth
def add():
    if request.method == 'GET':
        return render_template('add.html')
    name = request.form.get('name')
    age = request.form.get('age')
    DATA_DICT.update({randint(50, 100): {'name': name, 'age': age}})
    return redirect('/index')


@app.route('/delete')
@auth
def delete():
    nid = request.args.get('nid', type=int)
    del DATA_DICT[nid]
    return redirect('/index')

@app.route('/modify', methods=['GET', 'POST'])
@auth
def modify():
    nid = request.args.get('nid')
    nid = int(nid)

    if request.method == 'GET':
        info = DATA_DICT[nid]
        name = info['name']
        age = info['age']
        return render_template('/modify.html', name=name, age=age)
    
    name = request.form.get('name')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = name
    DATA_DICT[nid]['age'] = age
    #return redirect('/index')
    return redirect(url_for('idx'))


@app.route('/json')
@auth
def json():
    return jsonify({'code': 200, 'data': [1, 2, 3]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
