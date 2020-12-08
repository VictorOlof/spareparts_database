import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name):
    rf.add_model(mm.Supplier, supplier_name=supplier_name, supplier_address=supplier_address,
                 supplier_phone=supplier_phone, supplier_email=supplier_email,
                 contact_name=contact_name)


def get_all_suppliers():
    return rf.get_all_models(mm.Supplier)


def get_products_by_supplier(selected_supplier):
    return rf.get_model_by_id(mm.Supplier, selected_supplier)
