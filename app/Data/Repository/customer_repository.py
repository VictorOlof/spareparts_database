from Data.models.customer import Customer
from Data.db import session


def add_customer():
    return None


def get_all_customers():
    return session.query(Customer).all()
