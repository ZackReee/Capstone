from database import *
from sqlalchemy.sql import func
from mydt import get_time

class Transactions(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    t_id = db.Column(db.Integer, unique=False, nullable=False)
    buyer_nric = db.Column(db.String(10), unique=False, nullable=False)
    product_name = db.Column(db.String(120), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    sub_total = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    discount = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    tax = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    grand_total = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    datetime = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Transaction %r>' % self.id
    
    def __init__(self, t_id, nric, product_name, qty, sub_total, discount, tax, g_total, dt):
        self.t_id = t_id
        self.buyer_nric = nric
        self.product_name = product_name
        self.quantity= qty
        self.sub_total = sub_total
        self.discount = discount
        self.tax = tax
        self.grand_total = g_total
        self.datetime = dt
        
        
def drop_transactions_table():
    try:
        print("dropping Transactions table")
        Transactions.__table__.drop(db_engine)
    except:
        print('the table "Transactions" does not exist')
        
def populate_transactions():
    t1 = Transactions(1, "S9606192G", "POKKA Premium Milk Tea", 1, 1.6, 5, 7, 6.40, get_time())
    t2 = Transactions(1, "S9606192G", "POKKA Premium Milk Coffee", 1, 1.6, 5, 7, 6.40, get_time())
    t3 = Transactions(1, "S9606192G", "POKKA Premium Cappuccino", 2, 3.2, 5, 7, 6.40, get_time())


    # try:
    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)
    # db.session.add(t4)
    db.session.commit()
    # except:
    #     print("Duplicate key in database")

def get_next_t_id():
    t = Transactions.query.order_by(Transactions.t_id).all()
    print("this: ", t)
    
    for i in t:
        print(i.product_name)
        