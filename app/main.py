from db import Base, engine, session
from models.address import Address
from models.customer import Customer


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


def show_all_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(customer)


def show_all_addresses():
    pass


def show_test():
    records = session.query(Customer).\
        join(Address, Customer.customer_address_id == Address.address_id).all()
    for record in records:
        record_object = {
            'Name': record.first_name,
            'Address': record.address.address,
            'City': record.address.city
        }
        print(record_object)

    for cname, customer_address_id, address_id in session.query(Customer.first_name, Customer.customer_address_id,
                                                                Address.address_id):
        print(cname, customer_address_id, address_id)

    for row in session.query(Customer, Customer.first_name).all():
        print(row.Customer, row.first_name)

    for c, a in session.query(Customer, Address). \
            filter(Customer.customer_address_id). \
            filter(Address.address_id). \
            all():
        print(c, a)


def main():
    Base.metadata.create_all(engine)

    # add_customer()
    # show_all_customers()
    # show_all_addresses()
    show_test()

if __name__ == '__main__':
    main()
