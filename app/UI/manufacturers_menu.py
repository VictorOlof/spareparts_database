from Controllers.manufacturers_controller import add_manufacturer, get_all_manufacturers


def manufacturer_menu():
    while True:
        print("Manufacturers menu")
        print("----------")
        print("1. Add info to manufacturers")
        print("2. Show all manufacturers")

        select = input("> ")
        if select == "1":
            manufacturer_id = input("Enter manufacturer id: ")
            manufacturer_name = input("Enter manufacturer name: ")
            hq_address = input('Enter hq_address: ')
            hq_phone = input('Enter hq phone: ')
            contact_name = int(input('Enter contact name: '))
            contact_phone = input('Enter contact phone: ')
            contact_email = input('Enter contact email: ')

            add_manufacturer(manufacturer_id, manufacturer_name, hq_address, hq_phone, contact_name, contact_phone
                             , contact_email)

        elif select == "2":
            manufacturers = get_all_manufacturers()
            for manufacturer in manufacturers:
                print(manufacturer)
        else:
            break
