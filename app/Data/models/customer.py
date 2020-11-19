from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100), nullable=False)
    customer_address_id = sa.Column(sa.Integer, sa.ForeignKey('addresses.address_id'))

    address = relationship("Address", back_populates="customer")
    # customers_has_car_models = relationship("CustomerCar", back_populates="customers")

    def __repr__(self):
        return f'Customer: {self.customer_id}, {self.first_name}'
