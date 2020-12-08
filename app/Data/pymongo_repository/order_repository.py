import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf
from bson import ObjectId


def create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id):
    obj_temp = rf.add_model(mm.Order, order_date=order_date, required_date=required_date, shipped_date=shipped_date,
                            status=status, comment=comment, employee_id=employee_id, customer_id=customer_id)
    add_customer_to_order(obj_temp.order_id, customer_id)


def add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each):
    product = rf.get_model_by_id(mm.Product, product_id)
    rf.insert_items_to_embedded_list(mm.Order, order_id, 'order_details', {'product_id': product_id,
                                                                           'product_name': product.product_name,
                                                                           'quantity_ordered': quantity_ordered,
                                                                           'sell_price_each': sell_price_each})


def get_all_orders():
    return rf.get_all_models(mm.Order)


def add_customer_to_order(order_id, customer_id):
    customer = rf.get_model_by_id(mm.Customer, customer_id)
    rf.insert_items_to_embedded_field(mm.Order, order_id, 'customer', {'first_name': customer.first_name,
                                                                       'last_name': customer.last_name,
                                                                       'address': customer.address,
                                                                       'city': customer.city,
                                                                       'postal_code': customer.postal_code,
                                                                       'country': customer.country})
