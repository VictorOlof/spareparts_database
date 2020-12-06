from Data.models.product import Product
from Data.Repository import repo_functions as rf


def add_product(product_name, description, quantity_in_stock, storage_space, buy_price, product_supplier_id,
                product_category_id, product_manufacturer_id):
    rf.add_model(Product, product_name=product_name, description=description, quantity_in_stock=quantity_in_stock,
                 storage_space=storage_space, buy_price=buy_price, product_supplier_id=product_supplier_id,
                 product_category_id=product_category_id, product_manufacturer_id=product_manufacturer_id)


def get_all_products():
    return rf.get_all_models(Product)


def get_product_by_id(product_id):
    return rf.get_model_by_id(Product, 'product_id', product_id)
