from flask import Flask, render_template, jsonify, request, redirect, url_for
from random import randint
app = Flask(__name__)

DATA_DICT = {
    1: {'name': 'Feix', 'age': 40},
    2: {'name': 'Daniel', 'age': 38}
}

@app.route('/index', endpoint='idx')
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
        return redirect('/index')
    
    error = '用户名或者密码错误'
    warning = '警告信息！'
    return render_template('login.html', error=error, warning=warning)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    name = request.form.get('name')
    age = request.form.get('age')
    DATA_DICT.update({randint(50, 100): {'name': name, 'age': age}})
    return redirect('/index')


@app.route('/delete')
def delete():
    nid = request.args.get('nid', type=int)
    del DATA_DICT[nid]
    return redirect('/index')

@app.route('/modify', methods=['GET', 'POST'])
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
def json():
    return jsonify({'code': 200, 'data': [1, 2, 3]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
