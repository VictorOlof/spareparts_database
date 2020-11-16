from db import Base, engine, session
from models.parents import Parent
from models.children import Child
from models.address import Address
from models.customer import Customer


def add_customer():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    address = input('Enter street address: ')
    city = input('Enter city: ')
    postal_code = int(input('Enter postal code: '))
    country = input('Enter country: ')

    address = Address(address=address, city=city, postalCode=postal_code, country=country)
    customer = Customer(first_name=first_name, last_name=last_name, customer_address_id=1)
    session.add(address)
    session.add(customer)
    session.commit()


def show_all_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(customer)


def show_all_addresses():
    addresses = session.query(Address).all()
    for address in addresses:
        print(address)


def main():
    Base.metadata.create_all(engine)

    add_customer()
    show_all_customers()


if __name__ == '__main__':
    main()
