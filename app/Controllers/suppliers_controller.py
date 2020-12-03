import Data.Repository.supplier_repository as su


def add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name):
    su.add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name)


def get_all_suppliers():
    return su.get_all_suppliers()


def get_products_by_supplier(selected_supplier):
    return su.get_products_by_supplier(selected_supplier)


