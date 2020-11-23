import Data.Repository.customer_car_repository as ccr


def add_customer_car(customer_id, car_model_id, reg_plate, color):
    ccr.add_customer_car(customer_id, car_model_id, reg_plate, color)


def get_all_customer_car():
    return ccr.get_all_customer_car()