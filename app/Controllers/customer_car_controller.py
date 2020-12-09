import Data.pymongo_repository.customer_car_repository as p_cc


def add_customer_car(customer_id, car_model_id, reg_plate, color):
    p_cc.add_customer_car(customer_id, car_model_id, reg_plate, color)


def get_all_customer_car():
    pass  # return ccr.get_all_customer_car()


def get_customer_car_by_id(customer_id):
    pass  # return ccr.get_customer_car_by_id(customer_id)


def get_car_by_reg_plate(reg_plate):
    pass  # return ccr.get_car_by_reg_plate(reg_plate)


def get_customer_by_customer_car(customer_car_obj):
    pass  # return ccr.get_customer_by_customer_car(customer_car_obj)
