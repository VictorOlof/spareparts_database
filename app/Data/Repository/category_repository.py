from Data.db import session
from Data.models.category import Category


def add_category(category_name, category_description):
    category = Category(category_name=category_name, category_description=category_description)

    session.add(category)
    session.commit()


def get_all_categories():
    return session.query(Category).all()


def get_products_by_category():  # TODO filter products on category
    # return session.query(Category).filter(JOIN products.product_category_id ON categories.category_id).all()
    pass
