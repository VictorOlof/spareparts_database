from Data.models.car_brand import CarBrand
from Data.db import session


def add_car_brand(car_brand_name):
    car_brand = CarBrand(car_brand_name=car_brand_name)
    session.add(car_brand)
    session.commit()


def get_all_car_brands():
    return session.query(CarBrand).all()
