import Data.pymongo_repository.customer_repository as p_cr


def add_customer(first_name, last_name, address_name, city, postal_code, country, company_name, org_number):
    p_cr.add_customer(first_name, last_name, address_name, city, postal_code, country, company_name, org_number)


def get_all_customers():
    return p_cr.get_all_customers()


def update_customer_by_column(customer_obj, column_value, value):
    p_cr.update_customer_by_column(customer_obj, column_value, value)


def get_customer_by_id(customer_id):
    return p_cr.get_customer_by_id(customer_id)


def remove_customer(obj):
    p_cr.remove_customer(obj)


def get_customer_by_car(car_obj):
    pass  # return cr.get_customer_by_car(car_obj)
