import Data.Repository.customer_repository as cr


def add_customer(first_name, last_name, address_name, city, postal_code, country):
    cr.add_customer(first_name, last_name, address_name, city, postal_code, country)


def get_all_customers():
    return cr.get_all_customers()


def update_customer_address(obj, address, city, postal_code, country):
    cr.update_customer_address(obj, address, city, postal_code, country)


def get_customer_by_id(customer_id):
    return cr.get_customer_by_id(customer_id)