import Data.pymongo_repository.car_brand_repository as p_cb
import Data.pymongo_repository.car_model_repository as p_cm


def add_car_model_and_brand(car_brand_name, car_model_name, car_model_year):
    obj_temp = p_cb.add_car_brand(car_brand_name)
    p_cm.add_car_model(obj_temp, car_model_name, car_model_year)
