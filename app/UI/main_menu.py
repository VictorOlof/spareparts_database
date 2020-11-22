from UI.customers_menu import customers_menu
from UI.orders_menu import orders_menu


def main_menu():
    while True:
        print("Main menu")
        print("----------")
        print("1. Customers")
        print("2. Orders")

        select = input("> ")
        if select == "1":
            customers_menu()
        elif select == "2":
            orders_menu()
        else:
            break
