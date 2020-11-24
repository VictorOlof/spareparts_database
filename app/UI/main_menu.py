from UI.customers_menu import customers_menu
from UI.orders_menu import orders_menu
from UI.car_menu import car_menu


def main_menu():
    while True:
        print("Main menu")
        print("----------")
        print("1. Customers")
        print("2. Orders")
        print("3. Cars menu")

        select = input("> ")
        if select == "1":
            customers_menu()
        elif select == "2":
            orders_menu()
        elif select == "3":
            car_menu()
        else:
            break
