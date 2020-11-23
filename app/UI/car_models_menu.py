from Controllers.car_model_controller import add_car_model, get_all_car_models


def car_models_menu():
    while True:
        print("Car Models menu")
        print("----------")
        print("1. Add info to car models")
        print("2. Show all car models")

        select = input("> ")
        if select == "1":
            car_model_name = input("Enter model name: ")
            car_model_year = input("Enter model year: ")
            car_model_car_brand_id = int(input('Enter brand id: '))

            add_car_model(car_model_name, car_model_year, car_model_car_brand_id)

        elif select == "2":
            car_models = get_all_car_models()
            for car_model in car_models:
                print(car_model)
        else:
            break
