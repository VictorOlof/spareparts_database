from Controllers.customer_car_controller import add_customer_car, get_all_customer_car, get_car_by_reg_plate, \
    get_customer_by_customer_car
from Controllers.product_car_controller import add_product_car
from Controllers.carbrands_controller import add_car_brand, get_all_car_brands, get_brand_by_model
from Controllers.car_model_controller import add_car_model, get_all_car_models_by_brand, get_model_by_car, \
    get_all_car_models

from UI.menu_functions import get_user_option_by_dict_keys, print_table, print_all_key_value_in_dict


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
        print("8. View all car models for car brand")

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
            customer_car = get_car_by_reg_plate(reg_plate)
            if customer_car:
                table_items = [
                    {'Reg. Plate': customer_car.reg_plate.upper(),
                     'First name': get_customer_by_customer_car(customer_car).first_name.capitalize(),
                     'Last name': get_customer_by_customer_car(customer_car).last_name.capitalize()}
                ]
                print_table(table_items)
            else:
                print(f"Could not found any owner with reg. plate: {reg_plate.upper()}")

        elif select == "6":  # View owners for all cars
            customer_cars = get_all_customer_car()
            if customer_cars:
                table_items = [
                    {'Reg. Plate': customer_car.reg_plate.upper(),
                     'Model': get_model_by_car(customer_car).car_model_name.capitalize(),
                     'Year': str(get_model_by_car(customer_car).car_model_year),
                     'First name': get_customer_by_customer_car(customer_car).first_name.capitalize(),
                     'Last name': get_customer_by_customer_car(customer_car).last_name.capitalize()}
                    for customer_car in customer_cars
                ]
                print_table(table_items)
            else:
                print("Could not find any cars.")

        elif select == "7":  # View all car models
            car_models = get_all_car_models()
            if car_models:
                table_items = [
                    {'Brand': get_brand_by_model(car_model).car_brand_name.capitalize(),
                     'Model': car_model.car_model_name,
                     'Year': str(car_model.car_model_year)}
                    for car_model in car_models
                ]
                print_table(table_items)
            else:
                print("Could not find any car models")

        elif select == "8":  # View all car models for car brand
            car_brands = get_all_car_brands()
            if car_brands:
                print("Select car brand")
                print_all_key_value_in_dict(
                    {key: car_brand.car_brand_name.capitalize()
                     for key, car_brand in car_brands.items()}
                )

                select = get_user_option_by_dict_keys(car_brands)
                selected_brand = car_brands[select]
                car_models = get_all_car_models_by_brand(selected_brand)

                if car_models:
                    table_items = [
                        {'Model': car_model.car_model_name,
                         'Year': str(car_model.car_model_year)}
                        for car_model in car_models
                    ]
                    print_table(table_items)
                else:
                    print(f"Could not find any models for {selected_brand.car_brand_name.capitalize()} brand.")
            else:
                print(f"Could not find any car brands.")

        else:
            break
