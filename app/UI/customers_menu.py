from Controllers.customers_controller import add_customer, get_all_customers, \
    get_customer_by_id, remove_customer, get_customers_by_column_value, update_customer_by_column, \
    get_customer_columns
from UI.menu_functions import print_table, get_object_info, print_menu, get_user_option_by_dict_keys


def customers_menu():
    print("Customer Menu")
    print("------------")
    while True:
        options_main = {
            "1": ("Add info to customers", add_info_to_customer),
            "2": ("Show all customers", show_all_customers),
            "3": ("Update address for customer", update_address_for_customer),
            "4": ("Delete customer", delete_customer),
            "5": ("Leave menu", None)
        }

        print_menu(options_main)
        option = get_user_option_by_dict_keys(options_main)
        try:
            options_main[option][1]()
        except TypeError:
            break  # Leave menu if not able to call


def add_info_to_customer():
    customer_info = get_object_info(columns=get_customer_columns(),
                                    column_skip='customer_id')
    add_customer(*customer_info)


def show_all_customers():
    customers = get_all_customers()
    if customers:
        table_items = [
            {'First name': str(customer.first_name),
             'Last name': str(customer.last_name),
             'Address': str(customer.address),
             'City': str(customer.city),
             'Postal code': str(customer.postal_code),
             'Country': str(customer.country),
             'Company': str(customer.company_name),
             'Org. Number': str(customer.org_number)}
            for customer in customers
        ]
        print_table(table_items)
    else:
        print("Could not find any customers.")


def update_address_for_customer():
    customer_id = input("Enter customer id: ")
    customer = get_customer_by_id(customer_id)
    get_customers_by_column_value('customer_id', customer_id)

    update_columns = ['address', 'city', 'postal_code', 'country']
    for column in update_columns:
        value = input(f"Enter new {column}: ")
        update_customer_by_column(customer, column, value)


def delete_customer():
    customer_id = input("Enter customer id: ")
    customer = get_customer_by_id(customer_id)
    remove_customer(customer)
