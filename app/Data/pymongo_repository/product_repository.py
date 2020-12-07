import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_product(product_name, description, quantity_in_stock, storage_space, buy_price, product_supplier_id,
                product_category_id, product_manufacturer_id):
    product = mm.Product({'product_name': product_name, 'description': description,
                          'quantity_in_stock': quantity_in_stock, 'storage_space': storage_space,
                          'buy_price': buy_price, 'product_supplier_id': product_supplier_id,
                          'product_category_id': product_category_id,
                          'product_manufacturer_id': product_manufacturer_id})
    product.save()


def get_all_products():
    return rf.get_all_models(mm.Product)
