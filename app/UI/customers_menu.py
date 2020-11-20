from Controllers.customers_controller import add_customer, get_all_customers


def customers_menu():
    while True:
        print("Customers menu")
        print("----------")
        print("1. Add info to customers")
        print("2. Show all customers")

        select = input("> ")
        if select == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address_name = input('Enter street address: ')
            city = input('Enter city: ')
            postal_code = int(input('Enter postal code: '))
            country = input('Enter country: ')

            add_customer(first_name, last_name, address_name, city, postal_code, country)

        elif select == "2":
            customers = get_all_customers()
            for customer in customers:
                print(customer)
        else:
            break
