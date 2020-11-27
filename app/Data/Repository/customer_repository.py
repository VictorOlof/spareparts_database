from Data.models.customer import Customer
from Data.db import session


def add_customer(first_name, last_name, address_name, city, postal_code, country, company_name, org_number):
    customer = Customer(first_name=first_name, last_name=last_name, address=address_name,
                        city=city, postal_code=postal_code, country=country,
                        company_name=company_name, org_number=org_number)
    session.add(customer)
    session.commit()


def get_all_customers():
    return session.query(Customer).all()


def update_customer_address(obj, address, city, postal_code, country):
    setattr(obj, 'address', address)
    setattr(obj, 'city', city)
    setattr(obj, 'postal_code', postal_code)
    setattr(obj, 'country', country)
    session.add(obj)
    session.commit()


def get_customer_by_id(customer_id):
    return session.query(Customer).get(customer_id)


def remove_customer(obj):
    session.delete(obj)
    session.commit()


def get_customer_by_car(car_obj):
    return car_obj.customer
