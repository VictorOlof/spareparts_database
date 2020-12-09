import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_product_car(product_id, car_model_id):
    rf.add_model(mm.ProductCar, product_id=product_id, car_model_id=car_model_id)


def get_all_product_car():
    return rf.get_all_models(mm.ProductCar)
