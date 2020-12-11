from Controllers.customer_car_controller import add_customer_car, get_all_customer_car, get_car_by_reg_plate, \
    get_customer_by_customer_car, get_customer_car_columns
from Controllers.product_car_controller import add_product_car, get_product_car_columns
from Controllers.carbrands_controller import add_car_brand, get_all_car_brands, get_brand_by_model, get_brand_columns
from Controllers.car_model_controller import add_car_model, get_all_car_models_by_brand, get_model_by_car, \
    get_all_car_models, get_car_model_columns

from UI.menu_functions import get_user_option_by_dict_keys, print_table, print_all_key_value_in_dict, get_object_info, \
    print_menu


def car_menu():
    print("Car Menu")
    print("------------")
    while True:
        options_main = {
            "1": ("Add car to customer", add_car_to_customer),
            "2": ("Add car to product", add_car_to_product),
            "3": ("Create new car brand", create_new_car_brand),
            "4": ("Create new car model", create_new_car_model),
            "5": ("Search car owner by reg. plate", search_car_owned_by_reg_plate),
            "6": ("View owners for all cars", view_owners_for_all_cars),
            "7": ("View all car models", view_all_car_models),
            "8": ("View all car models for car brand", view_all_car_models_for_car_brand),
            "9": ("Leave menu", None)
        }

        print_menu(options_main)
        option = get_user_option_by_dict_keys(options_main)
        try:
            options_main[option][1]()
        except TypeError:
            break  # Leave menu if not able to call


def add_car_to_customer():
    customer_car_info = get_object_info(columns=get_customer_car_columns())
    add_customer_car(*customer_car_info)


def add_car_to_product():
    product_car_info = get_object_info(columns=get_product_car_columns())
    add_product_car(*product_car_info)


def create_new_car_brand():
    car_brand_info = get_object_info(columns=get_brand_columns(),
                                     column_skip='car_brand_id')
    add_car_brand(*car_brand_info)


def create_new_car_model():
    car_model_info = get_object_info(columns=get_car_model_columns(),
                                     column_skip='car_model_id')
    add_car_model(*car_model_info)


def search_car_owned_by_reg_plate():
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


def view_owners_for_all_cars():
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


def view_all_car_models():
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


def view_all_car_models_for_car_brand():
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
