from Controllers.carbrands_controller import add_car_brand, get_all_car_brands


def car_brands_menu():
    while True:
        print("Car brands menu")
        print("----------")
        print("1. Add info to car brands")
        print("2. Show all car brands")

        select = input("> ")
        if select == "1":
            car_brand_name = input("Enter brand name: ")

            add_car_brand(car_brand_name=car_brand_name)

        elif select == "2":
            car_brands = get_all_car_brands()
            for car_brand in car_brands:
                print(car_brand)
        else:
            break
