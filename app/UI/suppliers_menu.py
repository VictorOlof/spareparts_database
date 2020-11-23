from Controllers.suppliers_controller import add_supplier, get_all_suppliers


def suppliers_menu():
    while True:
        print("Suppliers Menu")
        print("==============")
        print("1. Add Supplier")
        print("2. Show All Suppliers")
        print("3. Show Available Carparts By Supplier")
        print("4. Quit Suppliers Menu")

        selection = input("> ")
        if selection == "1":
            supplier_name = input('Supplier name: ')
            supplier_address = input('Supplier address: ')
            supplier_phone = input('Supplier phone: ')
            supplier_email = input('Supplier email: ')
            contact_name = input('Contact name: ')

            add_supplier(supplier_name, supplier_address, supplier_phone, supplier_email, contact_name)

        elif selection == "2":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
        elif selection == "3":
            selected_supplier = input("Select a supplier: ")
            print(selected_supplier)
        else:
            break
