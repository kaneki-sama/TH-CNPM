from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pysql://root:123456@localhost/appsale?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = True

db = SQLAlchemy(app=app)
admin= Admin(app=app, name='IT82 SHOP')