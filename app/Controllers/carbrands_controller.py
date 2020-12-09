import Data.pymongo_repository.car_brand_repository as p_cb


def add_car_brand(car_brand_name):
    p_cb.add_car_brand(car_brand_name)


def get_all_car_brands():
    car_brands = p_cb.get_all_car_brands()
    return {str(i+1): car_brand for i, car_brand in enumerate(car_brands)}
    # return {str(i+1): car_brand for i, car_brand in enumerate(car_brands)}


def get_brand_by_model(car_model_obj):
    pass
    # return cbr.get_brand_by_model(car_model_obj)
