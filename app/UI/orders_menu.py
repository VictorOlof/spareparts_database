from Controllers.orders_controller import add_order, get_all_orders


def orders_menu():
    while True:
        print("Orders Menu")
        print("===========")
        print("1. Add Info To Orders")
        print("2. View All Orders")

        print("5. Quit Orders Menu")

        selection = input(" >")
        if selection == "1":
            order_date = input('Order date: ')
            required_date = input('Required date: ')
            shipped_date = input('Shipped date: ')
            status = input('Status: ')
            comment = input('Comment: ')
            employee_id = int(input('Employee id: '))
            customer_id = int(input('Customer id: '))

            add_order(order_date, required_date, shipped_date, status, comment, employee_id, customer_id)

        elif selection == "2":
            orders = get_all_orders()
            for order in orders:
                print(order)
        else:
            break
