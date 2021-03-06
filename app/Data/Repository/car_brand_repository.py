from Data.models.car_brand import CarBrand
from Data.Repository import repo_functions as rf


def add_car_brand(car_brand_name):
    rf.add_model(CarBrand, car_brand_name=car_brand_name)


def get_all_car_brands():
    return rf.get_all_models(CarBrand)


def get_brand_by_model(car_model_obj):
    return car_model_obj.car_brand


def get_brand_columns():
    return rf.get_object_columns(CarBrand)