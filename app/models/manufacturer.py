from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    manufacturer_id = sa.Column(sa.Integer, primary_key=True)
    manufacturer_name = sa.Column(sa.String(50), nullable=False)
    hq_address = sa.Column(sa.String(50), nullable=False)
    hq_phone = sa.Column(sa.String(50), nullable=False)
    contact_name = sa.Column(sa.String(50))
    contact_phone = sa.Column(sa.String(50))
    contact_email = sa.Column(sa.String(50))

    # address = relationship("Address", back_populates="customer")

    def __repr__(self):
        return f'Manufacturer: {self.manufacturer_id}, {self.manufacturer_name}, {self.hq_address}, {self.hq_phone},' \
               f' {self.contact_name}, {self.contact_phone}, {self.contact_email}'
