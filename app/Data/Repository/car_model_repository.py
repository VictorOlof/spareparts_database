from Data.models.car_model import CarModel
from Data.db import session
from Data.Repository import repo_functions as rf


def add_car_model(car_model_name, car_model_year, car_model_car_brand_id):
    car_model = CarModel(car_model_name=car_model_name, car_model_year=car_model_year,
                         car_model_car_brand_id=car_model_car_brand_id)
    session.add(car_model)
    session.commit()


def get_all_car_models():
    return rf.get_all_models(CarModel)


def get_all_car_models_by_brand(car_brand_obj):
    return car_brand_obj.car_models


def get_model_by_car(car_obj):
    return car_obj.car_model
