from UI.customers_menu import customers_menu
from UI.orders_menu import orders_menu
# from UI.carbrand_menu import car_brands_menu
from UI.car_models_menu import car_models_menu


def main_menu():
    while True:
        print("Main menu")
        print("----------")
        print("1. Customers")
        print("2. Orders")
        print("3. Car brands")
        print("4. Car Models menu")

        select = input("> ")
        if select == "1":
            customers_menu()
        elif select == "2":
            orders_menu()
        elif select == "3":
            #  car_brands_menu()
            pass
        elif select == "4":
            car_models_menu()
        else:
            break
