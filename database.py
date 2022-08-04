from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

DB_URI = 'mysql://root:password@localhost/pos'
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]= DB_URI
db = SQLAlchemy(app)
db_engine = create_engine(DB_URI)