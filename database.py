from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]= 'mysql://root:password@localhost/pos'
db = SQLAlchemy(app)
db_engine = create_engine('mysql://root:password@localhost/pos')