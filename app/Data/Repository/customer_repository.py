from Data.models.customer import Customer
from Data.db import session


def add_customer(first_name, last_name, address_name, city, postal_code, country):
    customer = Customer(first_name=first_name, last_name=last_name, address=address_name,
                        city=city, postal_code=postal_code, country=country)
    session.add(customer)
    session.commit()


def get_all_customers():
    return session.query(Customer).all()
