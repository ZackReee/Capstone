from itertools import product
from sqlalchemy.sql import func
from login import db

class Transactions(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    t_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    product_name = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    total_price = db.Column(db.Numeric(10, 2), unique=True, nullable=False)
    t_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<Transaction %r>' % self.name