import Data.Repository.product_repository as pr


def add_product(product_name, description, quantity_in_stock, storage_space, buy_price,
                product_supplier_id, product_category_id, product_manufacturer_id):
    pr.add_product(product_name, description, quantity_in_stock, storage_space, buy_price,
                   product_supplier_id, product_category_id, product_manufacturer_id)


def get_all_products():
    return pr.get_all_products()


def get_product_by_id(product_id):
    return pr.get_product_by_id(product_id)