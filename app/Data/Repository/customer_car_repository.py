from Data.models.customers_has_carmodels import CustomerCar
from Data.db import session


def add_customer_car(customer_id, car_model_id, reg_plate, color):
    customer_car = CustomerCar(customer_id=customer_id, car_models_id=car_model_id,
                               reg_plate=reg_plate, color=color)
    session.add(customer_car)
    session.commit()


def get_all_customer_car():
    return session.query(CustomerCar).all()


def get_customer_car_by_id(customer_id):
    return session.query(CustomerCar).filter(CustomerCar.customer_id == customer_id).all()


def get_car_by_reg_plate(reg_plate):
    return session.query(CustomerCar).filter(CustomerCar.reg_plate == reg_plate).first()
