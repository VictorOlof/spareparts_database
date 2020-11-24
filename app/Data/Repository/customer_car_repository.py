from Data.models.customers_has_carmodels import CustomerCar
from Data.models.customer import Customer
from Data.models.order import Order
from Data.db import session


def add_customer_car(customer_id, car_model_id, reg_plate, color):
    customer_car = CustomerCar(customer_id=customer_id, car_models_id=car_model_id,
                               reg_plate=reg_plate, color=color)
    session.add(customer_car)
    session.commit()


def get_all_customer_car():
    return session.query(CustomerCar).all()


def get_customer_car_by_id(customer_id):
    return session.query(Customer, Order).filter(Customer.customer_id == Order.customer_id)
    # return session.query(CustomerCar).filter(CustomerCar.customer_id == customer_id).all()


"""dict 
for c, o in session.query(Customer, Order).filter(Customer.customer_id == Order.customer_id):
    print(type(c))
    print(f'Ordernumber: {o.order_id}, Customer: {c.first_name}, Orderdate: {o.order_date}')
"""
"""result = get_customer_car_by_id(1)
for res in result:
    print(type(res))

result_l = [p for (p, ) in session.query(Customer, Order).filter(Customer.customer_id == Order.customer_id)]
print(result_l)"""
