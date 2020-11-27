from Controllers.customers_controller import add_customer, get_all_customers, \
    get_customer_by_id, update_customer_address, remove_customer
from UI.menu_functions import print_table


def customers_menu():
    while True:
        print("Customers menu")
        print("----------")
        print("1. Add info to customers")
        print("2. Show all customers")
        print("3. Update address for customer")
        print("4. Remove customer")

        select = input("> ")
        if select == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input('Enter street address: ')
            city = input('Enter city: ')
            postal_code = int(input('Enter postal code: '))
            country = input('Enter country: ')
            company_name = input("Enter company_name: ")
            org_number = input("Enter organisation number: ")
            add_customer(first_name, last_name, address, city, postal_code, country, company_name, org_number)

        elif select == "2":
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

        elif select == "3":  # Update address for customer
            customer_id = input("Enter customer id: ")
            customer = get_customer_by_id(customer_id)
            address = input('Enter street address: ')
            city = input('Enter city: ')
            postal_code = input('Enter postal code: ')
            country = input('Enter country: ')
            update_customer_address(customer, address, city, postal_code, country)

        elif select == "4":  # 4. Remove customer
            customer_id = input("Enter customer id: ")
            customer = get_customer_by_id(customer_id)
            remove_customer(customer)

        else:
            break

