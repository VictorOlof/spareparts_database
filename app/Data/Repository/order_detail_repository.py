from Data.db import session
from Data.models.order_detail import OrderDetail
from Data.Repository import repo_functions as rf


def add_order_detail(order_id, product_id, quantity_ordered, sell_price_each):
    rf.add_model(OrderDetail, order_id=order_id, product_id=product_id, quantity_ordered=quantity_ordered,
                 sell_price_each=sell_price_each)


def get_all_order_details(order_id):
    return session.query(OrderDetail).filter(OrderDetail.order_id == order_id).first()


