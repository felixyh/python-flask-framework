[TOC]

# Flask Web Course

## Quick Start

### A quick sample
```python
from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

@app.route('/index')
def index():
    return "首页"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template('login.html')

    user = request.form.get('user')
    password = request.form.get('password')
    if user == 'felix' and password == 'novirus':
        return redirect('/index')
    
    error = '用户名或者密码错误'
    return render_template('login.html', error=error)


@app.route('/json')
def json():
    return jsonify({'code': 200, 'data': [1, 2, 3]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

