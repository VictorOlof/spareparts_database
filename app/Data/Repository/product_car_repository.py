from Data.models.products_has_carmodels import ProductCar
from Data.db import session
from Data.Repository import repo_functions as rf


def add_product_car(product_id, car_model_id):
    product_car = ProductCar(product_id, car_model_id)
    session.add(product_car)
    session.commit()


def get_all_product_car():
    return rf.get_all_models(ProductCar)
