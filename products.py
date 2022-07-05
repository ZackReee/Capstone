from database import *

class Products(db.Model):
    __tablename__ = "products"
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    category_id = db.Column(db.Integer, unique=False, nullable=False)
    barcode = db.Column(db.String(45), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return '<Products %r>' % self.name

    def __init__(self, name, price, cat, bar, desc):
        self.name = name
        self.unit_price = price
        self.category_id = cat
        self. barcode= bar
        self.description = desc

def populate_products():
    p1 = Products("Green-Tea 500ml", 1.20, 1, "8888196124128", "500ml Can")
    p2 = Products("Coke 500ml less sugar", 1.20, 1, "12345678", "500ml can less sugar")
    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()
    except:
        print("Duplicate key in database")

def drop_products_table():
    try:
        print("dropping products table")
        Products.__table__.drop(db_engine)
    except:
        print('the table "Products" does not exist')

def get_product(barcode):
    p = Products.query.filter_by(barcode=barcode).first()
    return p