from database import *

class Products(db.Model):
    __tablename__ = "products"
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    category_id = db.Column(db.Integer, unique=False, nullable=False)
    barcode = db.Column(db.String(45), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return '<Products %r>' % self.name

    def __init__(self, name, price, cat, bar, desc):
        self.name = name
        self.price = price
        self.category_id = cat
        self.barcode= bar
        self.description = desc

# add products in here
def populate_products():
    p1 = Products("POKKA Premium Milk Coffee", 1.60, 1, "8888196303912", "500ml Bottle")
    p2 = Products("POKKA Premium Milk Tea", 1.60, 1, "8888196303813", "500ml Bottle")
    p3 = Products("POKKA Premium Cappuccino", 1.60, 1, "8888196305916", "500ml Bottle")
    p4 = Products("F&N Blueberry Cranberry, Fruit Tree Fresh", 2.00, 1, "8888200615543", "250ml Bottle")
    p5 = Products("POKKA Premium Mocha", 1.60, 1, "8888196903211", "500ml Bottle")
    p6 = Products("POKKA Ice Peach Tea", 2.10, 1, "8888196172419", "1.5litre Bottle")
    
    # include them for the commit in here
    my_products = [p1,p2,p3,p4,p5,p6]
    try:
        for i in my_products:
            db.session.add(i)

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
    print(p, ", ", p.name, ", $", p.price)
    return p
