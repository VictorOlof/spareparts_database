from Controllers.order_details_controller import get_all_order_details
from Controllers.orders_controller import create_order, get_all_orders, create_employee, create_store, add_item_to_order


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

        selection = input(" >")
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
            print(order_details)

        elif selection == "6":
            orders = get_all_orders()
            for order in orders:
                print(order)
        elif selection == "7":
            break
