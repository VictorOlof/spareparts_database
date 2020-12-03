from Data.db import session
from Data.models.manufacturer import Manufacturer
from Data.models.product import Product


def add_manufacturer(manufacturer_name, hq_address, hq_phone, contact_name,
                     contact_phone, contact_email):
    manufacturer = Manufacturer(manufacturer_name=manufacturer_name,
                                hq_address=hq_address, hq_phone=hq_phone, contact_name=contact_name,
                                contact_phone=contact_phone, contact_email=contact_email)
    session.add(manufacturer)
    session.commit()


def get_all_manufacturers():
    return session.query(Manufacturer).all()


def get_products_by_manufacturer(selected_manufacturer):
    return session.query(Manufacturer, Product).filter(Manufacturer.manufacturer_id == Product.product_manufacturer_id)\
        .filter(Manufacturer.manufacturer_name == selected_manufacturer).all()
