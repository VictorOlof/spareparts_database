from Data.db import session
from Data.models.category import Category
from Data.models.product import Product
from Data.Repository import repo_functions as rf


def add_category(category_name, category_description):
    rf.add_model(Category, category_name=category_name, category_description=category_description)


def get_all_categories():
    return rf.get_all_models(Category)


def get_products_by_category(category):
    return session.query(Category, Product).filter(Category.category_id == Product.product_category_id).filter\
        (Category.category_name == category).all()

