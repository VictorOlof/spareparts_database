import Data.Repository.customer_car_repository as ccr


def add_customer_car(customer_id, car_model_id, reg_plate, color):
    ccr.add_customer_car(customer_id, car_model_id, reg_plate, color)


def get_all_customer_car():
    return ccr.get_all_customer_car()


def get_customer_car_by_id(customer_id):
    return ccr.get_customer_car_by_id(customer_id)


def get_car_by_reg_plate(reg_plate):
    return ccr.get_car_by_reg_plate(reg_plate)