import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_car_brand(car_brand_name):
    return rf.add_model(mm.CarBrand, car_brand_name=car_brand_name)


def get_all_car_brands():
    return rf.get_all_models(mm.CarBrand)


def get_brand_by_model(car_model_obj):
    pass  # return car_model_obj.car_brand
