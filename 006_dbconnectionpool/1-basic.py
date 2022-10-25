from flask import Flask, render_template
import pymysql
from config import Config

app = Flask(__name__, template_folder='./')

@app.route('/index')
def index():
    conn = pymysql.connect(host='192.168.0.113', port=3006, user='root', passwd=Config.MYSQL_PASSWD, db='chevereto')
    cursor = conn.cursor()
    cursor.execute("select * from images")
    
    result = cursor.fetchall()
    
    # conn.commit()
    cursor.close()
    conn.close()
    #print(result)

    return render_template('index.html', result=result)


@app.route('/login')
def login():
    conn = pymysql.connect(host='192.168.0.113', port=3006, user='root', passwd=Config.MYSQL_PASSWD, db='chevereto')
    cursor = conn.cursor()
    cursor.execute("select * from images")
    
    result = cursor.fetchall()
    
    # conn.commit()
    cursor.close()
    conn.close()
    #print(result)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



