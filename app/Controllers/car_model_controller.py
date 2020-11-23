import Data.Repository.car_model_repository as cmr


def add_car_model(car_model_name, car_model_year, car_model_car_brand_id):
    cmr.add_car_model(car_model_name, car_model_year, car_model_car_brand_id)


def get_all_car_models():
    return cmr.get_all_car_models()