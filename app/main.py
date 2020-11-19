from Data.db import Base, engine, session
from Data.models.address import Address
from Data.models.car_brand import CarBrand
from Data.models.car_model import CarModel
from Data.models.customer import Customer
from Data.models.customers_has_carmodels import CustomerCar


def add_customer():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    address_name = input('Enter street address: ')
    city = input('Enter city: ')
    postal_code = int(input('Enter postal code: '))
    country = input('Enter country: ')

    address = Address(address_name=address_name, city=city, postal_code=postal_code, country=country)
    session.add(address)
    session.commit()

    customer = Customer(first_name=first_name, last_name=last_name, customer_address_id=address.address_id)
    session.add(customer)
    session.commit()


def main():
    Base.metadata.create_all(engine)

    add_customer()


if __name__ == '__main__':
    main()
