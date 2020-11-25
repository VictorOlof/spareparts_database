from Controllers.categories_controller import add_category, get_all_categories, get_products_by_category


def categories_menu():
    while True:
        print("Categories Menu")
        print("===============")
        print("1. Add Category")
        print("2. Show All Categories")
        print("3. Show Carparts By Category")

        selection = input("> ")
        if selection == "1":
            category_name = input('Category name: ')
            category_description = input('Category description: ')

            add_category(category_name, category_description)

        elif selection == "2":
            categories = get_all_categories()
            for category in categories:
                print(category)
        elif selection == "3":
            category = input("Select a category: ")
            products = get_products_by_category(category)
            print(products) # TODO fix print out
        elif selection == "4":
            break
