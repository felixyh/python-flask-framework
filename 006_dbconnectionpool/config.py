import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MYSQL_PASSWD = os.getenv('MYSQL_PASSWD', 'None')