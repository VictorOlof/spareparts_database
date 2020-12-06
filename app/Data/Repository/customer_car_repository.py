from Data.models.customers_has_carmodels import CustomerCar
from Data.db import session
from Data.Repository import repo_functions as rf


def add_customer_car(customer_id, car_model_id, reg_plate, color):
    customer_car = CustomerCar(customer_id=customer_id, car_models_id=car_model_id,
                               reg_plate=reg_plate, color=color)
    session.add(customer_car)
    session.commit()


def get_all_customer_car():
    return rf.get_all_models(CustomerCar)


def get_customer_car_by_id(customer_id):
    return rf.get_model_by_column_value(CustomerCar, 'customer_id', customer_id)


def get_car_by_reg_plate(reg_plate):
    return rf.get_model_by_column_value(CustomerCar, 'reg_plate', reg_plate)


def get_customer_by_customer_car(customer_car_obj):
    return customer_car_obj.customer
