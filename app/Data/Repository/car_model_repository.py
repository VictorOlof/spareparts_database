from Data.models.car_model import CarModel
from Data.db import session


def add_car_model(car_model_name, car_model_year, car_model_car_brand_id):
    car_model = CarModel(car_model_name=car_model_name, car_model_year=car_model_year,
                         car_model_car_brand_id=car_model_car_brand_id)
    session.add(car_model)
    session.commit()


def get_all_car_models():
    return session.query(CarModel).all()


def get_all_car_models_by_brand(car_brand_obj):
    return car_brand_obj.car_models
