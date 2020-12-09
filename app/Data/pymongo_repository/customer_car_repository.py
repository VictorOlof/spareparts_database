import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_customer_car(customer_id, car_model_id, reg_plate, color):
    car = rf.get_model_by_id(mm.CarModel, car_model_id)
    rf.insert_items_to_embedded_list(mm.Customer, customer_id, "cars", {"car_id": car_model_id,
                                                                        "car_brand_name": car.car_brand_name,
                                                                        "car_model_name": car.car_model_name,
                                                                        "car_model_year": car.car_model_year,
                                                                        "reg_plate": reg_plate,
                                                                        "color": color})



def get_all_customer_car():
    pass  # return rf.get_all_models(CustomerCar)


def get_customer_car_by_id(customer_id):
    pass  # return rf.get_model_by_id(CustomerCar, 'customer_id', customer_id)


def get_car_by_reg_plate(reg_plate):
    pass  # return rf.get_model_by_id(CustomerCar, 'reg_plate', reg_plate)


def get_customer_by_customer_car(customer_car_obj):
    pass  # return customer_car_obj.customer
