from Data.models.customer import Customer
from Data.Repository import repo_functions as rf


def add_customer(first_name, last_name, address_name, city, postal_code, country, company_name, org_number):
    rf.add_model(Customer, first_name=first_name, last_name=last_name, address=address_name, city=city,
                 postal_code=postal_code, country=country, company_name=company_name, org_number=org_number)


def get_all_customers():
    return rf.get_all_models(Customer)


def get_customer_by_id(customer_id):
    return rf.get_model_by_column_value(Customer, 'customer_id', customer_id)


def get_customers_by_column_value(column_value, value):
    return rf.get_models_by_column_value(Customer, column_value, value)


def update_customer_by_column(customer_obj, column_value, value):
    rf.update_object_by_column(customer_obj, column_value, value)


def remove_customer(customer_obj):
    rf.remove_object(customer_obj)


def get_customer_by_car(car_obj):
    return car_obj.customer
