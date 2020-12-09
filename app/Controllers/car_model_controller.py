import Data.pymongo_repository.car_model_repository as p_cm


def add_car_model(car_model_name, car_model_year, car_model_car_brand_id):
    p_cm.add_car_model(car_model_name, car_model_year, car_model_car_brand_id)


def get_all_car_models():
    pass  # return p_cm.get_all_car_models()


def get_all_car_models_by_brand(car_brand_obj):
    pass  # return cmr.get_all_car_models_by_brand(car_brand_obj)
    # {car_model for car_model in car_models}


def get_model_by_car(car_obj):
    pass  # return cmr.get_model_by_car(car_obj)
