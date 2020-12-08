import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_category(category_name, category_description):
    rf.add_model(mm.Category, category_name=category_name, category_description=category_description)


def get_all_categories():
    return rf.get_all_models(mm.Category)


def get_products_by_category(category):
    return rf.get_model_by_id(mm.Category, category)
