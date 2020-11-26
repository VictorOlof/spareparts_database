import Data.Repository.car_brand_repository as cbr


def add_car_brand(car_brand_name):
    cbr.add_car_brand(car_brand_name)


def get_all_car_brands():
    car_brands = cbr.get_all_car_brands()
    return {i+1: car_brand for i, car_brand in enumerate(car_brands)}
