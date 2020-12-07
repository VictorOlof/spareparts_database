from Controllers.products_controller import add_product, get_all_products, get_all_products_by_car_model
from Controllers.car_model_controller import add_car_model, get_all_car_models
from UI.menu_functions import print_table

from UI.menu_functions import get_user_option_by_dict_keys, print_table, print_all_key_value_in_dict


def product_menu():
    while True:
        print("Products menu")
        print("----------")
        print("1. Add info to products")
        print("2. Show all products")
        print("3. Show all products for car model")

        select = input("> ")
        if select == "1":
            product_id = int(input("Enter product id: "))
            product_name = input("Enter product name: ")
            description = input('Enter description: ')
            quantity_in_stock = int(input('Enter quantity in stock: '))
            storage_space = int(input('Enter storage space: '))
            buy_price = int(input('Enter buy price: '))
            product_supplier_id = int(input('Enter product supplier id: '))
            product_category_id = int(input('Enter product category id: '))
            product_manufacturer_id = int(input('Enter manufacturer id: '))

            add_product(product_id, product_name, description, quantity_in_stock, storage_space, buy_price,
                        product_supplier_id, product_category_id, product_manufacturer_id)

        elif select == "2":
            products = get_all_products()
            if products:
                table_items = [
                    {'Product id': str(product.id),
                     'Product name': str(product.name),
                     'Description': str(product.description),
                     'Quantity in stock': str(product.quantity_in_stock),
                     'Storage space': str(product.storage_space),
                     'Buy price': str(product.buy_price),
                     'product supplier id': str(product.supplier_id),
                     'Product category id': str(product.category_id),
                     'Product manufacturer id': str(product.manufacturer_id)}
                    for product in products
                ]
                print_table(table_items)
            else:
                print("Could not find any customers.")

        elif select == "3": # View all products for car model
            car_models = get_all_car_models()
            if car_models:
                print("Select car model")
                print_all_key_value_in_dict(
                    {key: car_model.capitalize()
                    for key, car_model in car_models.items()}

                )

                select = get_user_option_by_dict_keys(car_models)
                selected_model = car_models[select]
                car_models = get_all_products_by_car_model(selected_model)

                if car_models:
                    table_items = [
                        {'Model': car_model.car_model_name,
                        'Year': str(car_model.car_model_year)}
                        for car_model in car_models
                    ]
                    print_table(table_items)
                else:
                    print(f"Could not find any models for {selected_model.car_model_name.capitalize()} model.")
            else:
                print(f"Could not find any car models.")

        else:
            break
