import Data.Repository.manufacturer_repository as mr


def add_manufacturer(manufacturer_name, hq_address, hq_phone, contact_name, contact_phone,
                     contact_email):
    mr.add_manufacturer(manufacturer_name, hq_address, hq_phone, contact_name, contact_phone,
                        contact_email)


def get_all_manufacturers():
    return mr.get_all_manufacturers()


def get_products_by_manufacturer(selected_manufacturer):
    return mr.get_products_by_manufacturer(selected_manufacturer)
