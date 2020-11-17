from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = 'addresses'

    address_id = sa.Column(sa.Integer, primary_key=True)
    address_name = sa.Column(sa.String(100), nullable=False)
    city = sa.Column(sa.String(100), nullable=False)
    postal_code = sa.Column(sa.Integer, nullable=False)
    country = sa.Column(sa.String(100), nullable=False)

    customer = relationship("Customer", back_populates="address")

    def __repr__(self):
        return f'Address: {self.address_id}, {self.address_name}'
