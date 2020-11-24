from Controllers.customer_car_controller import add_customer_car, get_car_by_reg_plate
from Controllers.product_car_controller import add_product_car
from Controllers.carbrands_controller import add_car_brand, get_all_car_brands
from Controllers.car_model_controller import add_car_model
from Controllers.customers_controller import get_all_customers


def car_menu():
    while True:
        print("Car menu")
        print("--------")
        print("1. Add car to customer")
        print("2. Add car to product")
        print("3. Create new car brand")
        print("4. Create new car model")
        print("5. Search car owner by reg. plate")
        print("6. View owners for all cars")
        print("7. View all car models")

        select = input("> ")

        if select == "1":  # Add car to customer
            customer_id = int(input('Enter customer id: '))
            car_model_id = int(input('Enter car model id: '))
            reg_plate = input("Enter registration plate: ")
            color = input("Enter color: ")
            add_customer_car(customer_id, car_model_id, reg_plate, color)

        elif select == "2":  # Add car to product
            product_id = int(input('Enter product id: '))
            car_model_id = int(input('Enter car model id: '))
            add_product_car(product_id, car_model_id)

        elif select == "3":  # Create new car brand
            car_brand_name = input("Enter brand name: ")
            add_car_brand(car_brand_name=car_brand_name)

        elif select == "4":  # Create new car model
            car_model_name = input("Enter model name: ")
            car_model_year = input("Enter model year: ")
            car_model_car_brand_id = int(input('Enter brand id: '))
            add_car_model(car_model_name, car_model_year, car_model_car_brand_id)

        elif select == "5":  # Search car owner by reg. plate
            reg_plate = input("Enter reg. plate: ")
            car = get_car_by_reg_plate(reg_plate)
            if car:
                print('{:12}{:12}{:12}'.format('Reg. Plate', 'First name', 'Last name'))
                print('{:12}{:12}{:12}'.format(car.reg_plate.upper(),
                                               car.customer.first_name.capitalize(),
                                               car.customer.last_name.capitalize()))
            else:
                print(f"Could not found any owner with reg. plate: {reg_plate.upper()}")

        elif select == "6":  # View owners for all cars
            customers = get_all_customers()
            for cu in customers:
                if cu.cars:
                    print('{:12}{:12}{:12}{:12}{:12}{:12}'.format('Reg. Plate', 'Car brand', 'Car model', 'Car color',
                                                                  'First name', 'Last name'))
                    for cc in cu.cars:
                        print('{:12}{:12}{:12}{:12}{:12}{:12}'.format(cc.reg_plate.upper(),
                                                                      cc.car_model.car_brand.
                                                                      car_brand_name.capitalize(),
                                                                      cc.car_model.car_model_name,
                                                                      cc.color.capitalize(),
                                                                      cu.first_name, cu.last_name))

        elif select == "7":  # View all car models
            car_brands = get_all_car_brands()
            print('{:12}{:12}{}'.format('Brand', 'Model', 'Year'))
            for cb in car_brands:
                for cm in cb.car_models:
                    print('{:12}{:12}{}'.format(cb.car_brand_name.capitalize(),
                                                cm.car_model_name,
                                                cm.car_model_year))

        else:
            break

