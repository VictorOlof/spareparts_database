from Data.db import session
from Data.models.manufacturer import Manufacturer


def add_manufacturer(manufacturer_id, manufacturer_name, hq_address, hq_phone, contact_name,
                     contact_phone, contact_email):
    manufacturer = Manufacturer(manufacturer_id=manufacturer_id, manufacturer_name=manufacturer_name,
                                hq_address=hq_address, hq_phone=hq_phone, contact_name=contact_name,
                                contact_phone=contact_phone, contact_email=contact_email)
    session.add(manufacturer)
    session.commit()


def get_all_manufacturers():
    return session.query(Manufacturer).all()
