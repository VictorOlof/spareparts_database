from Controllers.categories_controller import get_products_by_category
from Controllers.products_controller import add_product, get_all_products, get_product_by_id
from Controllers.suppliers_controller import add_supplier, get_all_suppliers, get_products_by_supplier
from Controllers.manufacturers_controller import add_manufacturer, get_all_manufacturers, get_products_by_manufacturer
from Controllers.product_orders_controller import add_product_order, get_product_order_by_id
from UI.menu_functions import print_table, print_menu, get_user_option_by_dict_keys


def product_menu():
    print("Product Menu")
    print("------------")
    while True:
        options_main = {
            "1": ("Add info to products", add_info_to_products),
            "2": ("Add info to supplier", add_info_to_supplier),
            "3": ("Add info to manufacturer", add_info_to_manufacturer),
            "4": ("View all products", view_all_products),
            "5": ("View all products by category", view_all_products_by_category),
            "6": ("View all products by supplier", view_all_products_by_supplier),
            "7": ("View all products by manufacturer", view_all_products_by_manufacturer),
            "8": ("Create auto-order for product", create_auto_order_for_product),
            "9": ("Leave menu", None)
        }

        print_menu(options_main)
        option = get_user_option_by_dict_keys(options_main)
        try:
            options_main[option][1]()
        except TypeError:
            break  # Leave menu if not able to call


def add_info_to_products():
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


def add_info_to_supplier():
    supplier_name = input('Supplier name: ')
    supplier_address = input('Supplier address: ')
    supplier_phone = input('Supplier phone: ')
    supplier_email = input('Supplier email: ')
    contact_name = input('Contact name: ')

    add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name)


def add_info_to_manufacturer():
    manufacturer_name = input("Enter manufacturer name: ")
    hq_address = input('Enter hq_address: ')
    hq_phone = input('Enter hq phone: ')
    contact_name = int(input('Enter contact name: '))
    contact_phone = input('Enter contact phone: ')
    contact_email = input('Enter contact email: ')

    add_manufacturer(manufacturer_name, hq_address, hq_phone, contact_name, contact_phone, contact_email)


def view_all_products():
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


def view_all_products_by_category():
    category = input("Select a category: ")
    products = get_products_by_category(category)
    if products:
        for product in products:
            print(product)
    else:
        print(f'Could not find any products for category {category}.')


def view_all_products_by_supplier():
    list_suppliers = input('Select a supplier (Press "l" to list all suppliers): ')
    while list_suppliers != "l":
        list_suppliers = input('Press "l" to list all suppliers: ')
    else:
        suppliers = get_all_suppliers()
        if suppliers:
            table_items = [
                {'Supplier id': suppliers.supplier_id,
                 'Supplier name': suppliers.supplier_name}
                for suppliers in suppliers
            ]
            print_table(table_items)
        else:
            print(f"Could not find any supplier with suppliers id: {suppliers.supplier_id}")
    selected_supplier = input("Select supplier: ")
    products = get_products_by_supplier(selected_supplier)
    if products:
        if products:
            table_items = [
                {'Product name': str(product.product_name),
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
        print(f'Could not find any products for the supplier {selected_supplier}.')


def view_all_products_by_manufacturer():
    list_manufacturers = input('Select a manufacturer (Press "l" to list all manufacturers): ')
    while list_manufacturers != "l":
        list_manufacturers = input('Press "l" to list all manufacturers: ')
    else:
        manufacturers = get_all_manufacturers()
        if manufacturers:
            table_items = [
                {'Manufacturer id': manufacturers.manufacturer_id,
                 'Manufacturer name': manufacturers.manufacturer_name}
                for manufacturers in manufacturers
            ]
            print_table(table_items)
        else:
            print(f"Could not find any manufacturer with manufacturer id: {manufacturers.manufacturer_id}")
    selected_manufacturer = input("Select manufacturer: ")
    products = get_products_by_manufacturer(selected_manufacturer)
    if products:
        table_items = [
            {'Product name': product.product_name,
             'Description': product.description,
             'Quantity in stock': str(product.quantity_in_stock),
             'Storage space': product.storage_space,
             'Buy price': str(product.buy_price),
             'Supplier id': str(product.supplier_id),
             'Category id': str(product.category_id),
             'Manufacturer id': str(product.manufacturer_id)}
            for product in products
        ]
        print_table(table_items)
    else:
        print(f'Could not find any products for the manufacturer {selected_manufacturer}.')


def create_auto_order_for_product():
    input_id = input("Enter product id: ")
    product_order = get_product_order_by_id(input_id)
    product = get_product_by_id(input_id)
    if product_order:
        print("Auto-order for product already exist: ")
        table_items = [
            {'Product id': str(product_order.product_order_id),
             'Quantity limit': str(product_order.quantity_limit),
             'Order amount': str(product_order.order_amount),
             'Incoming date': str(product_order.order_incoming_date)}
        ]
        print_table(table_items)
        print("Change auto-order for product? Y/N")
        # TODO: change columns in product orders
    else:
        if product:
            quantity_limit = input("Enter quantity limit: ")
            order_amount = input("Enter order amount: ")
            order_incoming_date = input("Enter incoming date: ")
            add_product_order(input_id, quantity_limit, order_amount, order_incoming_date)
        else:
            print(f"Could not find any products for id {input_id}")
