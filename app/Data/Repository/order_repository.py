from Data.db import session
from Data.models.order import Order


def add_order(order_id, order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    order = Order(order_id=order_id, order_date=order_date, required_date=required_date,
                  shipped_date=shipped_date, status=status, comment=comment,
                  employee_id=employee_id, customer_id=customer_id)
    session.add(order)
    session.commit()


def get_all_orders():
    return session.query(Order).all()
