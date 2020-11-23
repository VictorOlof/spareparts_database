from Data.db import session
from Data.models.supplier import Supplier


def add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name):
    supplier = Supplier(supplier_name=supplier_name, supplier_address=supplier_address, supplier_phone=supplier_phone,
                        supplier_email=supplier_email, contact_name=contact_name)
    session.add(supplier)
    session.commit()


def get_all_suppliers():
    return session.query(Supplier).all()


def get_products_by_supplier():  # TODO filter products by supplier
    # return session.query.filter(JOIN Supplier.supplier_id ON Product.product_supplier_id)
    pass

