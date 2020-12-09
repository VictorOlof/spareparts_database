import Data.pymongo_repository.product_car_repository as pcr


def add_product_car(product_id, car_model_id):
    pcr.add_product_car(product_id, car_model_id)


def get_all_product_car():
    return pcr.get_all_product_car
