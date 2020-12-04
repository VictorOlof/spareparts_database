import Data.Repository.order_repository as od


def create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    od.create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id)


def add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each):
    od.add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each)


def get_all_orders():
    return od.get_all_orders()
