def print_menu(menu_options: dict):
    for key in menu_options.keys():
        print(f"{key}. {menu_options[key][0]}")


def get_user_option_by_dict_keys(menu_options: dict):
    while True:
        try:
            value = input("> ")
            if value not in menu_options.keys():
                raise ValueError
            else:
                return value
        except ValueError:
            print("Invalid option.")


def print_table(table: list):
    """Takes a list of dictionaries and print out values of dict in a table format"""
    # print table head row
    for key in table[0].keys():
        print('{:20}'.format(key), end="")
    print()
    # print rows
    for dic in table:
        for key in dic:
            value = dic[key]
            print('{:20}'.format(value), end="")
        print()
