import Data.Repository.category_repository as ca


def add_category(category_name, category_description):
    ca.add_category(category_name, category_description)


def get_all_categories():
    return ca.get_all_categories()


def get_products_by_category(category):
    return ca.get_products_by_category(category)

