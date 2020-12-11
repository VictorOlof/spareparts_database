from Controllers.employees_controller import create_employee
from Controllers.orders_controller import create_order, get_all_orders, add_item_to_order
from Controllers.order_details_controller import get_all_order_details
from Controllers.stores_controller import list_all_stores, create_store

from UI.menu_functions import print_table, print_menu, get_user_option_by_dict_keys


def orders_menu():
    print("Order Menu")
    print("------------")
    while True:
        options_main = {
            "1": ("Create New Order", create_new_order),
            "2": ("Create New Employee", create_new_employee),
            "3": ("Create New Store", create_new_store),
            "4": ("Add Item To Order", add_item_to_order_menu),
            "5": ("View All Items For Order", view_all_items_for_order),
            "6": ("View All Orders", view_all_orders),
            "7": ("Leave menu", None)
        }

        print_menu(options_main)
        option = get_user_option_by_dict_keys(options_main)
        try:
            options_main[option][1]()
        except TypeError:
            break  # Leave menu if not able to call


def create_new_order():
    order_date = input('Order date: ')
    required_date = input('Required date: ')
    shipped_date = input('Shipped date: ')
    status = input('Status: ')
    comment = input('Comment: ')
    employee_id = input('Employee id: ')
    customer_id = input('Customer id: ')

    create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id)


def create_new_employee():
    employee_name = input('Employee name: ')
    list_stores = input('Select store (Press "l" to list all stores): ')
    while list_stores != "l":
        list_stores = input('Press "l" to show all stores: ')
    else:
        stores = list_all_stores()
        print('{:15}{}'.format(str('Store id'), str('Store name')))
        for store in stores:
            print(store)

    employee_store_id = int(input('Store id: '))
    create_employee(employee_name, employee_store_id)


def create_new_store():
    store_name = input('Store name: ')
    create_store(store_name)


def add_item_to_order_menu():
    order_id = input('Order id: ')
    product_id = input('Product id: ')
    quantity_ordered = int(input('Quantity ordered: '))
    sell_price_each = float(input('Sell price each: '))

    add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each)


def view_all_items_for_order():
    order_id = input("Order id: ")
    order_details = get_all_order_details(order_id)
    if order_details:
        table_items = [
            {'Order id': order_detail.order_id,
             'Product id': order_detail.product_id,
             'Quantity ordered': order_detail.quantity_ordered,
             'Sell price each': order_detail.sell_price_each}
            for order_detail in order_details
        ]
        print_table(table_items)
    else:
        print(f"Could not find any order with order id: {order_id}")


def view_all_orders():
    orders = get_all_orders()
    if orders:
        table_items = [
            {'Order id': order.order_id,
             'Order date': str(order.order_date),
             'Shipped date': str(order.shipped_date),
             'Status': str(order.status),
             'Comment': str(order.comment),
             'Employee id': order.employee_id,
             'Customer id': order.customer_id}
            for order in orders
        ]
        print_table(table_items)
    else:
        print(f"Could not find any orders")
