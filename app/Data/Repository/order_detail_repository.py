from Data.db import session
from Data.models.order_detail import OrderDetail


def add_order_detail(order_id, product_id, quantity_ordered, sell_price_each):
    order_detail = OrderDetail(order_id=order_id, product_id=product_id, quantity_ordered=quantity_ordered,
                               sell_price_each=sell_price_each)
    session.add(order_detail)
    session.commit()


def get_all_order_details(order_id):
    return session.query(OrderDetail).filter(OrderDetail.order_id == order_id).first()


