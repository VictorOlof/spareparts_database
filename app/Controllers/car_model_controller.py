import Data.Repository.car_model_repository as cmr


def add_car_model(car_model_name, car_model_year, car_model_car_brand_id):
    cmr.add_car_model(car_model_name, car_model_year, car_model_car_brand_id)


def get_all_car_models():
    return cmr.get_all_car_models()


def get_all_car_models_by_brand(car_brand_obj):
    return cmr.get_all_car_models_by_brand(car_brand_obj)
    # {car_model for car_model in car_models}


def get_model_by_car(car_obj):
    return cmr.get_model_by_car(car_obj)