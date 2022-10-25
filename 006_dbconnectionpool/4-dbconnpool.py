from dbutils.pooled_db import PooledDB
import pymysql
from config import Config
from flask import Flask, render_template

from threading import Thread

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='192.168.0.113',
    port=3006,
    user='root',
    password=Config.MYSQL_PASSWD, 
    db='chevereto'
)

def task(num):
    # 从连接池中获取一个连接
    conn = POOL.connection()

    cursor = conn.cursor()
    cursor.execute('select sleep(3)') # 在数据库执行sleep 函数，hang住3秒
    result = cursor.fetchall()
    cursor.close()

    conn.close() # 将连接放回连接池，而不是关闭

    print(num, '------------->' ,result)




for i in range(57):
    t = Thread(target=task, args=(i, ))
    t.start()



# def fetchall(sql):
#     # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
#     # 否则
#     # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
#     # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
#     # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
#     # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
#     conn = POOL.connection()

#     # print(th, '链接被拿走了', conn1._con)
#     # print(th, '池子里目前有', pool._idle_cache, '\r\n')

#     cursor = conn.cursor()  # 创建游标，执行sql 语句
#     cursor.execute(sql)
#     result = cursor.fetchall()

#     cursor.close()

#     conn.close() # 将连接放回连接池，而不是关闭

#     return result

# @app.route('/login')
# def login():
#     result = fetchall('select * from images')

#     return render_template('index.html', result=result)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)