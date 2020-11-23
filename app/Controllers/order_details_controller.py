import Data.Repository.order_detail_repository as odd


def add_order_detail(order_id, product_id, quantity_ordered, sell_price_each, order_line_number):
    odd.add_order_detail(order_id, product_id, quantity_ordered, sell_price_each, order_line_number)


def get_all_order_details():
    return odd.get_all_order_details()