from Controllers.categories_controller import get_products_by_category
from Controllers.products_controller import add_product, get_all_products
from Controllers.suppliers_controller import add_supplier, get_all_suppliers, get_products_by_supplier
from Controllers.manufacturers_controller import add_manufacturer, get_all_manufacturers, get_products_by_manufacturer
from UI.menu_functions import print_table


def product_menu():
    while True:
        print("Products menu")
        print("----------")
        print("1. Add info to products")
        print("2. Add info to supplier")
        print("3. Add info to manufacturer")
        print("4. View all products")
        print("5. View all products by category")
        print("6. View all products by supplier")
        print("7. View all products by manufacturer")
        print("8. Quit Products Menu")

        select = input("> ")
        if select == "1":
            product_name = input("Enter product name: ")
            description = input('Enter description: ')
            quantity_in_stock = int(input('Enter quantity in stock: '))
            storage_space = int(input('Enter storage space: '))
            buy_price = int(input('Enter buy price: '))
            product_supplier_id = int(input('Enter product supplier id: '))
            product_category_id = int(input('Enter product category id: '))
            product_manufacturer_id = int(input('Enter manufacturer id: '))

            add_product(product_name, description, quantity_in_stock, storage_space, buy_price,
                        product_supplier_id, product_category_id, product_manufacturer_id)

        elif select == "2":
            supplier_name = input('Supplier name: ')
            supplier_address = input('Supplier address: ')
            supplier_phone = input('Supplier phone: ')
            supplier_email = input('Supplier email: ')
            contact_name = input('Contact name: ')

            add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name)

        if select == "3":
            manufacturer_name = input("Enter manufacturer name: ")
            hq_address = input('Enter hq_address: ')
            hq_phone = input('Enter hq phone: ')
            contact_name = int(input('Enter contact name: '))
            contact_phone = input('Enter contact phone: ')
            contact_email = input('Enter contact email: ')

            add_manufacturer(manufacturer_name, hq_address, hq_phone, contact_name, contact_phone, contact_email)

        elif select == "4":
            products = get_all_products()
            if products:
                table_items = [
                    {'Product name': str(product.product_name),
                     'Description': str(product.description),
                     'Quantity in stock': str(product.quantity_in_stock),
                     'Storage space': str(product.storage_space),
                     'Buy price': str(product.buy_price),
                     'Supplier id': product.product_supplier_id,
                     'Category id': product.product_category_id,
                     'Manufacturer id': product.product_manufacturer_id}
                    for product in products
                ]
                print_table(table_items)
            else:
                print(f"Could not find any products")

        elif select == "5":
            category = input("Select a category: ")
            products = get_products_by_category(category)
            if products:
                for product in products:
                    print(product)
            else:
                print(f'Could not find any products for category {category}.')

        elif select == "6":
            list_suppliers = input('Select a supplier (Press "l" to list all suppliers): ')
            while list_suppliers != "l":
                list_suppliers = input('Press "l" to list all suppliers: ')
            else:
                suppliers = get_all_suppliers()
                print('{:15}{}'.format(str('Store id'), str('Store name')))
                for supplier in suppliers:
                    print(supplier)
            selected_supplier = input("Select supplier: ")
            products = get_products_by_supplier(selected_supplier)
            if products:
                for product in products:
                    print(product)
            else:
                print(f'Could not find any products for the supplier {selected_supplier}.')

        elif select == "7":
            list_manufacturers = input('Select a manufacturer (Press "l" to list all manufacturers): ')
            while list_manufacturers != "l":
                list_manufacturers = input('Press "l" to list all manufacturers: ')
            else:
                manufacturers = get_all_manufacturers()
                print('{:15}{}'.format(str('Manufacturer id'), str('Manufacturer name')))
                for manufacturer in manufacturers:
                    print(manufacturer)
            selected_manufacturer = input("Select manufacturer: ")
            products = get_products_by_manufacturer(selected_manufacturer)
            if products:
                for product in products:
                    print(product)
            else:
                print(f'Could not find any products for the manufacturer {selected_manufacturer}.')

        elif select == "8":
            break
