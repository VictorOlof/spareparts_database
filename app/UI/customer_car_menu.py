from Controllers.customer_car_controller import add_customer_car, get_customer_car_by_id, get_all_customer_car


def customer_car_menu():
    while True:
        print("Customer to Car Menu")
        print("===========")
        print("1. Add car model to customer")
        print("2. View all cars for customer")
        print("3. View all cars for all customers")

        selection = input(" >")
        if selection == "1":
            customer_id = int(input('Enter customer id: '))
            car_model_id = int(input('Enter car model id: '))
            reg_plate = input("Enter registration plate: ")
            color = input("Enter color: ")

            add_customer_car(customer_id, car_model_id, reg_plate, color)

        elif selection == "2":
            customer_id = input("Enter customer id: ")
            customer_cars = get_customer_car_by_id(customer_id)
            for customer_car in customer_cars:
                print(customer_car)

        elif selection == "3":
            customer_cars = get_all_customer_car()
            for customer_car in customer_cars:
                print(customer_car)

        else:
            break