from UI.customers_menu import customers_menu
from UI.order_details_menu import order_details_menu


def main_menu():
    while True:
        print("Main menu")
        print("----------")
        print("1. Customers")

        select = input("> ")
        if select == "1":
            customers_menu()
            break
