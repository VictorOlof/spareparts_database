import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_car_model(car_model_name, car_model_year, car_model_car_brand_id):
    obj_temp = rf.get_model_by_id(mm.CarModel, car_model_car_brand_id)
    rf.add_model(mm.CarModel,
                 car_brand_name=obj_temp.car_brand_name,
                 car_model_name=car_model_name,
                 car_model_year=car_model_year)


def get_all_car_models():
    pass  # return rf.get_all_models(CarModel)


def get_all_car_models_by_brand(car_brand_obj):
    pass  # return car_brand_obj.car_models


def get_model_by_car(car_obj):
    pass  # return car_obj.car_model
