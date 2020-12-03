from Data.db import session
from Data.models.product import Product


def add_product(product_name, description, quantity_in_stock, storage_space, buy_price, product_supplier_id,
                product_category_id, product_manufacturer_id):
    manufacturer = Product(product_name=product_name, description=description,
                           quantity_in_stock=quantity_in_stock, storage_space=storage_space,
                           buy_price=buy_price, product_supplier_id=product_supplier_id,
                           product_category_id=product_category_id, product_manufacturer_id=product_manufacturer_id)
    session.add(manufacturer)
    session.commit()


def get_all_products():
    return session.query(Product).all()
