from Controllers.customers_controller import add_customer, get_all_customers, \
    get_customer_by_id, update_customer_address


def customers_menu():
    while True:
        print("Customers menu")
        print("----------")
        print("1. Add info to customers")
        print("2. Show all customers")
        print("3. Update address for customer")

        select = input("> ")
        if select == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input('Enter street address: ')
            city = input('Enter city: ')
            postal_code = int(input('Enter postal code: '))
            country = input('Enter country: ')

            add_customer(first_name, last_name, address, city, postal_code, country)

        elif select == "2":
            customers = get_all_customers()
            for customer in customers:
                print(customer)

        elif select == "3":  # Update address for customer
            customer_id = input("Enter customer id: ")
            customer = get_customer_by_id(customer_id)
            address = input('Enter street address: ')
            city = input('Enter city: ')
            postal_code = input('Enter postal code: ')
            country = input('Enter country: ')
            update_customer_address(customer, address, city, postal_code, country)

        else:
            break

