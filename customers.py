from database import *
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
    u1 = Customers("S9606192G", "Tom", "CPL", "Infantry", 23, 5.70, "Punggol Field 199D #13-437")
    try:
        db.session.add(u1)
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