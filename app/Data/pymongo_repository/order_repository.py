import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    order = mm.Order({'order_date': order_date, 'required_date': required_date, 'shipped_date': shipped_date,
                      'status': status, 'comment': comment, 'employee_id': employee_id, 'customer_id': customer_id})
    order.save()


def add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each):
    pass


def get_all_orders():
    return rf.get_all_models(mm.Order)
