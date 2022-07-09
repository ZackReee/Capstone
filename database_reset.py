from login import db
from products import *
from customers import Customers, populate_customers, drop_customers_table
from transactions import Transactions



drop_products_table()
drop_customers_table()

db.create_all()
populate_products()
populate_customers()