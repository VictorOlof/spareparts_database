from Data.db import session
from Data.models.product import Product
from Data.models.supplier import Supplier
from Data.Repository import repo_functions as rf


def add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name):
    rf.add_model(Supplier, supplier_name=supplier_name, supplier_address=supplier_address,
                 supplier_phone=supplier_phone, supplier_email=supplier_email, contact_name=contact_name)


def get_all_suppliers():
    return rf.get_all_models(Supplier)


def get_products_by_supplier(selected_supplier):
    return session.query(Supplier, Product).filter(Supplier.supplier_id == Product.product_supplier_id).filter \
        (Supplier.supplier_name == selected_supplier).all()
