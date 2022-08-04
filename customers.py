from database import *
import math
class Customers(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    nric = db.Column(db.String(9), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    rank = db.Column(db.String(30), unique=False, nullable=False)
    vocation = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    credit = db.Column(db.Numeric(6, 2), unique=False, nullable=False)
    address = db.Column(db.String(100), unique=False, nullable=False)

    def __init__(self, nric, name, rank, vocation, age, credit, address):
        self.nric = nric
        self.name = name
        self.rank = rank
        self.vocation = vocation
        self.age = age
        self.credit = credit
        self.address = address


def populate_customers():
    u1 = Customers("S1234567G", "Tom", "CPL", "Infantry", 23, 15.70, "Punggol Field 199D #11-437")
    u2 = Customers("S1111111A", "Jack", "3Sgt", "Infantry", 21, 24.70, "Tekong Street 123A")
    try:
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
    except:
        print("Duplicate key in database")

def drop_customers_table():
    try:
        print("dropping products table")
        Customers.__table__.drop(db_engine)
    except:
        print('Table "Customers" does not exist')

def get_cust_by_nric(n):
    u = Customers.query.filter_by(nric=n).first()
    return u


def deduct_credit(identity, val):
    u = Customers.query.filter_by(nric=identity).first()
    cred_f = float(u.credit)
    cred_f -= val
    print ("new val =", cred_f)
    cred_f = round_up(cred_f)
    u.credit = cred_f
    db.session.commit()
    
def round_up(n):
    new = "%.2f" % n
    return(new)
    # multiplier = 10 ** 2
    # return math.ceil(n * multiplier) / multiplier
    