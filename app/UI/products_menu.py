from Controllers.products_controller import add_product, get_all_products


def product_menu():
    while True:
        print("Products menu")
        print("----------")
        print("1. Add info to products")
        print("2. Show all products")
        print("3. Remove product")

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
            for product in products:
                print(product)
        else:
            break
