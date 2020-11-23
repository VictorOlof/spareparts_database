from Controllers.product_car_controller import add_product_car, get_all_product_car


def product_car_menu():
    while True:
        print("Products to Car Menu")
        print("===========")
        print("1. Add car model to product")
        print("2. View all products for car model")
        print("3. View all products for all car models")

        selection = input(" >")
        if selection == "1":
            product_id = int(input('Enter product id: '))
            car_model_id = int(input('Enter car model id: '))

            add_product_car(product_id, car_model_id)

        elif selection == "2":
            pass

        elif selection == "3":
            get_all_product_car()

        else:
            break
