from Data.db import session
from Data.models.manufacturer import Manufacturer
from Data.models.product import Product
from Data.Repository import repo_functions as rf


def add_manufacturer(manufacturer_name, hq_address, hq_phone, contact_name, contact_phone, contact_email):
    rf.add_model(Manufacturer, manufacturer_name=manufacturer_name, hq_address=hq_address, hq_phone=hq_phone,
                 contact_name=contact_name, contact_phone=contact_phone, contact_email=contact_email)


def get_all_manufacturers():
    return rf.get_all_models(Manufacturer)


def get_products_by_manufacturer(selected_manufacturer):
    return session.query(Manufacturer, Product).filter(Manufacturer.manufacturer_id == Product.product_manufacturer_id)\
        .filter(Manufacturer.manufacturer_name == selected_manufacturer).all()
