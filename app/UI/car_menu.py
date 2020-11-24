from Controllers.customer_car_controller import add_customer_car, get_customer_car_by_id
from Controllers.product_car_controller import add_product_car
from Controllers.carbrands_controller import add_car_brand
from Controllers.car_model_controller import add_car_model


def car_menu():
    while True:
        print("Car menu")
        print("--------")
        print("1. Add car to customer")
        print("2. Add car to product")
        print("3. Create new car brand")
        print("4. Create new car model")
        print("5. View cars for customer")
        print("6. View car models for product")

        select = input("> ")

        if select == "1":
            customer_id = int(input('Enter customer id: '))
            car_model_id = int(input('Enter car model id: '))
            reg_plate = input("Enter registration plate: ")
            color = input("Enter color: ")

            add_customer_car(customer_id, car_model_id, reg_plate, color)

        elif select == "2":
            product_id = int(input('Enter product id: '))
            car_model_id = int(input('Enter car model id: '))

            add_product_car(product_id, car_model_id)

        elif select == "3":
            car_brand_name = input("Enter brand name: ")
            add_car_brand(car_brand_name=car_brand_name)

        elif select == "4":
            car_model_name = input("Enter model name: ")
            car_model_year = input("Enter model year: ")
            car_model_car_brand_id = int(input('Enter brand id: '))

            add_car_model(car_model_name, car_model_year, car_model_car_brand_id)

        elif select == "5":
            customer_id = input("Enter customer id: ")
            customer_cars = get_customer_car_by_id(customer_id)
            for customer_car in customer_cars:
                print(customer_car)

        elif select == "6":
            pass

        else:
            break
