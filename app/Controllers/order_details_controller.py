import Data.pymongo_repository.order_detail_repository as p_od


def add_order_detail(order_id, product_id, quantity_ordered, sell_price_each):
    p_od.add_order_detail(order_id, product_id, quantity_ordered, sell_price_each)


def get_all_order_details(order_id):
    return p_od.get_all_order_details(order_id)
