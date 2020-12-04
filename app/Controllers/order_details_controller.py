import Data.Repository.order_detail_repository as odd


def add_order_detail(order_id, product_id, quantity_ordered, sell_price_each):
    odd.add_order_detail(order_id, product_id, quantity_ordered, sell_price_each)


def get_all_order_details(order_id):
    return odd.get_all_order_details(order_id)