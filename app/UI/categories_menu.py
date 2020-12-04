from Controllers.categories_controller import add_category, get_all_categories, get_products_by_category

from UI.menu_functions import print_table


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
            if categories:
                table_items = [
                    {'Category id': str(category.product_id),
                     'Category name': str(category.product_name),
                     'Description': str(category.description)}
                    for category in categories
                ]
                print_table(table_items)
            else:
                print("Could not find any categories.")

        elif selection == "3":
            category = input("Select a category: ")
            products = get_products_by_category(category)
            if products:
                table_items = [
                    {'Product id': str(product.product_id),
                     'Product name': str(product.product_name),
                     'Description': str(product.description),
                     'Quantity in stock': str(product.quantity_in_stock),
                     'Storage space': str(product.storage_space),
                     'Buy price': str(product.buy_price),
                     'Supplier id': str(product.supplier_id),
                     'Category id': str(product.category_id),
                     'Manufacturer id': str(product.manufacturer_id)}
                    for product in products
                ]
                print_table(table_items)
            else:
                print(f'Could not find any products for category {category}.')

        elif selection == "4":
            break
