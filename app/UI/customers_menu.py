from Controllers.customers_controller import add_customer, get_all_customers


def customers_menu():
    while True:
        print("Customers menu")
        print("----------")
        print("1. Add info to customers")
        print("2. Show all customers")

        select = input("> ")
        if select == "1":
            add_customer()
        elif select == "2":
            customers = get_all_customers()
            for customer in customers:
                print(customer)
        else:
            break
