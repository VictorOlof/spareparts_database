from Data.db import session
from Data.models.order_detail import OrderDetail


def add_order_detail(order_id, product_id, quantity_ordered, sell_price_each, order_line_number):
    order_detail = OrderDetail(order_id=order_id, product_id=product_id, quantity_ordered=quantity_ordered,
                               sell_price_each=sell_price_each, order_line_number=order_line_number)
    session.add(order_detail)
    session.commit()


def get_all_order_details():
    return session.query(OrderDetail).all()
