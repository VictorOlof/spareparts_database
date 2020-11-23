from Data.models.products_has_carmodels import ProductCar
from Data.db import session


def add_product_car(product_id, car_model_id):
    product_car = ProductCar(product_id, car_model_id)
    session.add(product_car)
    session.commit()


def get_all_product_car():
    return session.query(ProductCar).all()
