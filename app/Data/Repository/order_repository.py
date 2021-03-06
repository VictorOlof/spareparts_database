from Data.db import session
from Data.models.order import Order
from Data.models.order_detail import OrderDetail
from Data.Repository import repo_functions as rf


def create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    rf.add_model(Order, order_date=order_date, required_date=required_date, shipped_date=shipped_date, status=status,
                 comment=comment, employee_id=employee_id, customer_id=customer_id)


def add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each):
    added_item = OrderDetail(order_id=order_id, product_id=product_id,
                             quantity_ordered=quantity_ordered, sell_price_each=sell_price_each)

    session.add(added_item)
    session.commit()


def get_all_orders():
    return rf.get_all_models(Order)
