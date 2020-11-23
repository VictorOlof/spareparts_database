from Controllers.order_details_controller import get_all_order_details, add_order_detail


def order_details_menu():
    while True:
        print("Order Details Menu")
        print("==================")
        print("1. Add Order Details")
        print("2. Show All Order Details")
        print("3. Quit Order Details Menu")

        selection = input("> ")
        if selection == "1":
            order_id = int(input('Order id: '))
            product_id = int(input('Product name: '))
            quantity_ordered = int(input('Quantity ordered: '))
            sell_price_each = float(input('Sell price each: '))
            order_line_number = int(input('Order line number: '))

            add_order_detail(order_id, product_id, quantity_ordered, sell_price_each, order_line_number)

        elif selection == "2":
            order_details = get_all_order_details()
            for order_detail in order_details:
                print(order_detail)
        else:
            break
