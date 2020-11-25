def print_menu(menu_options: dict):
    for key in menu_options.keys():
        print(f"{key}. {menu_options[key][0]}")


def get_user_menu_option(menu_options: dict):
    while True:
        try:
            value = input("> ")
            if value not in menu_options.keys():
                raise ValueError
            else:
                return value
        except ValueError:
            print("Invalid option.")