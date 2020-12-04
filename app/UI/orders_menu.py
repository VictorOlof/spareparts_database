from Controllers.employees_controller import create_employee
from Controllers.orders_controller import create_order, get_all_orders, add_item_to_order
from Controllers.order_details_controller import get_all_order_details
from Controllers.stores_controller import list_all_stores, create_store

from UI.menu_functions import print_table


def orders_menu():
    while True:
        print("Orders Menu")
        print("===========")
        print("1. Create New Order")
        print("2. Create New Employee")
        print("3. Create New Store")
        print("4. Add Item To Order")
        print("5. View All Items For Order")
        print("6. View All Orders")
        print("7. Quit Orders Menu")

        selection = input("> ")
        if selection == "1":
            order_date = input('Order date: ')
            required_date = input('Required date: ')
            shipped_date = input('Shipped date: ')
            status = input('Status: ')
            comment = input('Comment: ')
            employee_id = int(input('Employee id: '))
            customer_id = int(input('Customer id: '))

            create_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id)

        elif selection == "2":
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

        elif selection == "3":
            store_name = input('Store name: ')
            create_store(store_name)

        elif selection == "4":
            order_id = int(input('Order id: '))
            product_id = int(input('Product id: '))
            quantity_ordered = int(input('Quantity ordered: '))
            sell_price_each = float(input('Sell price each: '))

            add_item_to_order(order_id, product_id, quantity_ordered, sell_price_each)

        elif selection == "5":
            order_id = int(input("Order id: "))
            order_details = get_all_order_details(order_id)
            if order_details:
                table_items = [
                    {'Order id': order_details.order_id,
                     'Product id': get_all_order_details(order_id).product_id,
                     'Quantity ordered': str(get_all_order_details(order_id).quantity_ordered),
                     'Sell price each': str(get_all_order_details(order_id).sell_price_each)}
                ]
                print_table(table_items)
            else:
                print(f"Could not find any order with order id: {order_id}")

        elif selection == "6":
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

        elif selection == "7":
            break
