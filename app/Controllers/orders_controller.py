import Data.Repository.order_repository as od


def create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    od.create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id)


def create_employee(employee_name, employee_store_id):
    od.create_employee(employee_name, employee_store_id)


def create_store(store_name):
    od.create_store(store_name)


def add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each):
    od.add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each)


def get_all_order_details(order_id):
    return od.get_all_order_details(order_id)


def get_all_orders():
    return od.get_all_orders()
