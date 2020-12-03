from UI.customers_menu import customers_menu
from UI.orders_menu import orders_menu
from UI.car_menu import car_menu
from UI.products_menu import product_menu
from UI.menu_functions import print_menu, get_user_option_by_dict_keys


def main_menu():
    while True:
        print("Main menu")
        print("---------")

        options_main = {
            "1": ("Customer menu", customers_menu),
            "2": ("Order menu", orders_menu),
            "3": ("Car menu", car_menu),
            "4": ("Product menu", product_menu),
            "5": ("Quit application", None)
        }

        print_menu(options_main)
        option = get_user_option_by_dict_keys(options_main)
        try:
            options_main[option][1]()
        except TypeError:
            break  # Leave menu if not able to call
