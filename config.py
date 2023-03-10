import os

BASE_DIR = os.path.dirname(__file__)

'''
    SQLALCHEMY_DATABASE_URI: DB 접속 주소
    SQLALCHEMY_TRACK_MODIFICATIONS: SQL_Alchemy의 이벤트를 처리하는 옵션 
'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'dev'

