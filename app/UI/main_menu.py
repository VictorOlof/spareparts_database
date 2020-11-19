from UI.customers_menu import customers_menu


def main_menu():
    while True:
        print("Main menu")
        print("----------")
        print("1. Customers")

        select = input("> ")
        if select == "1":
            customers_menu()
        else:
            break
