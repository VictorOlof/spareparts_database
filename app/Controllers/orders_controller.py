import Data.Repository.order_repository as od


def add_order(order_id, order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    od.add_order(order_id, order_date, required_date, shipped_date, status, comment, employee_id, customer_id)


def get_all_orders():
    return od.get_all_orders()