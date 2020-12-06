from Data.models.product_order import ProductOrder
from Data.Repository import repo_functions as rf


def add_product_order(product_order_id, quantity_limit, order_amount, order_incoming_date):
    rf.add_model(ProductOrder, product_order_id=product_order_id, quantity_limit=quantity_limit,
                 order_amount=order_amount, order_incoming_date=order_incoming_date)


def get_product_order_by_id(product_order_id):
    return rf.get_model_by_id(ProductOrder, 'product_order_id', product_order_id)
