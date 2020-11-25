from Data.db import session
from Data.models.category import Category
from Data.models.product import Product


def add_category(category_name, category_description):
    category = Category(category_name=category_name, category_description=category_description)

    session.add(category)
    session.commit()


def get_all_categories():
    return session.query(Category).all()


def get_products_by_category(category):
    return session.query(Category, Product).filter(Category.category_id == Product.product_category_id).filter\
        (Category.category_name == category).all()

