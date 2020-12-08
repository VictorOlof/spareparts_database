import Data.pymongo_repository.order_repository as p_o


def create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    obj_temp = p_o.create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id)
    p_o.add_customer_to_order(obj_temp.order_id, customer_id)


def add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each):
    p_o.add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each)


def get_all_orders():
    return p_o.get_all_orders()
