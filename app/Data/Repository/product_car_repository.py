from Data.models.products_has_carmodels import ProductCar
from Data.Repository import repo_functions as rf


def add_product_car(product_id, car_model_id):
    rf.add_model(ProductCar, product_id=product_id, car_model_id=car_model_id)


def get_all_product_car():
    return rf.get_all_models(ProductCar)


def get_product_car_columns():
    return rf.get_object_columns(ProductCar)
