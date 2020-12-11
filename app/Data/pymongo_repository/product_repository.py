import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_product(product_name, description, quantity_in_stock, storage_space, buy_price, product_supplier_id,
                product_category_id, product_manufacturer_id):
    obj_temp = rf.add_model(mm.Product, product_name=product_name, description=description,
                            quantity_in_stock=quantity_in_stock, storage_space=storage_space,
                            buy_price=buy_price, product_supplier_id=product_supplier_id,
                            product_category_id=product_category_id,
                            product_manufacturer_id=product_manufacturer_id)
    add_manufacturer_to_product(obj_temp.product_id, product_manufacturer_id)
    add_category_to_product(obj_temp.product_id, product_category_id)


def get_all_products():
    return rf.get_all_models(mm.Product)


def add_manufacturer_to_product(product_id, manufacturer_id):
    manufacturer = rf.get_model_by_id(mm.Manufacturer, manufacturer_id)
    rf.insert_items_to_embedded_field(mm.Product, product_id, 'manufacturer', {'manufacturer_name':
                                                                                   manufacturer.manufacturer_name,
                                                                               'hq_address':
                                                                                   manufacturer.hq_address,
                                                                               'hq_phone': manufacturer.hq_phone,
                                                                               'contact_name':
                                                                                   manufacturer.contact_name,
                                                                               'contact_phone':
                                                                                   manufacturer.contact_phone,
                                                                               'contact_email':
                                                                                   manufacturer.contact_email})


def add_category_to_product(product_id, category_id):
    category = rf.get_model_by_id(mm.Category, category_id)
    rf.insert_items_to_embedded_field(mm.Product, product_id, 'category', {'category_id': category_id,
                                                                           'category_name': category.category_name,
                                                                           'category_description':
                                                                               category.category_description})
