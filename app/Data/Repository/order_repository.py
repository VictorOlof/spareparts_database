from Data.db import session
from Data.models.order import Order
from Data.models.order_detail import OrderDetail


def create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    order = Order(order_date=order_date, required_date=required_date, shipped_date=shipped_date,
                  status=status, comment=comment, employee_id=employee_id, customer_id=customer_id)
    session.add(order)
    session.commit()


def add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each):
    added_item = OrderDetail(order_id=order_id, product_id=product_id,
                             quantity_ordered=quantity_ordered, sell_price_each=sell_price_each)

    session.add(added_item)
    session.commit()


def get_all_orders():
    return session.query(Order).all()
