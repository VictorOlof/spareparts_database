import Data.Repository.customer_repository as cr


def add_customer(first_name, last_name, address_name, city, postal_code, country):
    cr.add_customer(first_name, last_name, address_name, city, postal_code, country)


def get_all_customers():
    return cr.get_all_customers()
