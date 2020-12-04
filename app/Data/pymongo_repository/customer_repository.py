# from Data.pymongo_models import Customer
import Data.pymongo_models as mm


def add_customer(first_name, last_name, address_name, city, postal_code, country, company_name, org_number):
    customer = mm.Customer({'first_name': first_name, 'last_name': last_name, 'address': address_name,
                            'city': city, 'postal_code': postal_code, 'country': country,
                            'company_name': company_name, 'org_number': org_number})
    customer.save()


def get_all_customers():
    print(mm.Customer.all())
    return mm.Customer.all()


def get_customer_by_id(customer_id):
    pass


def get_customers_by_column_value(column_value, value):
    pass


def update_customer_by_column(customer_obj, column_value, value):
    pass


def remove_customer(customer_obj):
    pass


def get_customer_by_car(car_obj):
    pass
