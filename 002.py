from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

DATA_DICT = {
    '1': {'name': 'Feix', 'age': 40},
    '2': {'name': 'Daniel', 'age': 38}
}



@app.route('/index')
def index():
    data_dict = DATA_DICT
    return render_template('index.html', data_dict=data_dict)

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

@app.route('/edit')
def edit():
    nid = request.args.get('nid')
    print(nid)
    return 'edit'
<<<<<<< HEAD

@app.route('/delete')
def delete():
    nid = request.args.get('nid')
    print(nid)
    del DATA_DICT[nid]
    return redirect('/index')
=======
>>>>>>> e486f32cea0a95761d20ada6c2c8088ef717e518

@app.route('/delete')
def delete():
    nid = request.args.get('nid')
    print(nid)
    return 'delete'

@app.route('/json')
def json():
    return jsonify({'code': 200, 'data': [1, 2, 3]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
