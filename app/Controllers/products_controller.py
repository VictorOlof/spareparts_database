import Data.pymongo_repository.product_repository as p_p


def add_product(product_name, description, quantity_in_stock, storage_space, buy_price,
                product_supplier_id, product_category_id, product_manufacturer_id):
    p_p.add_product(product_name, description, quantity_in_stock, storage_space, buy_price,
                product_supplier_id, product_category_id, product_manufacturer_id)


def get_all_products():
    return p_p.get_all_products()


def get_product_by_id(product_id):
    pass  # return pr.get_product_by_id(product_id)