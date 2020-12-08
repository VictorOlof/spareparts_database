import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def add_order_detail(order_id, product_id, quantity_ordered, sell_price_each):
    pass
    """order_detail = OrderDetail(order_id=order_id, product_id=product_id, quantity_ordered=quantity_ordered,
                               sell_price_each=sell_price_each)
    session.add(order_detail)
    session.commit()"""


def get_all_order_details(order_id):
    return rf.create_items_from_embedded_list(
        model_obj=mm.Order,
        obj_id=order_id,
        list_name="order_details",
        create_obj=mm.OrderDetail
    )


