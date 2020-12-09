import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_car_model(model_obj, car_model_name, car_model_year):
    rf.update_object_by_column(model_obj=model_obj,
                               column_value='car_model_name',
                               value=car_model_name)
    rf.update_object_by_column(model_obj=model_obj,
                               column_value='car_model_year',
                               value=car_model_year)


def get_all_car_models():
    pass  # return rf.get_all_models(CarModel)


def get_all_car_models_by_brand(car_brand_obj):
    pass  # return car_brand_obj.car_models


def get_model_by_car(car_obj):
    pass  # return car_obj.car_model
