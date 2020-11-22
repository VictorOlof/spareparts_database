from Controllers.order_details_controller import get_all_order_details


def order_details_menu():
    while True:
        print("Order Details Menu")
        print("==================")
        print("1. Add Order Details")
        print("2. Show All Order Details")
        print("3. Quit Order Details Menu")

        selection = input("> ")
        if selection == "1":
            order_details = get_all_order_details()
            for order_detail in order_details:
                print(order_detail)
        else:
            break
