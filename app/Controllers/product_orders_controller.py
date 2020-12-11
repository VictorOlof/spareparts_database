def add_product_order(product_order_id, quantity_limit, order_amount, order_incoming_date):
    por.add_product_order(product_order_id, quantity_limit, order_amount, order_incoming_date)


def get_product_order_by_id(product_order_id):
    return por.get_product_order_by_id(product_order_id)