from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100), nullable=False)
    address = sa.Column(sa.String(100), nullable=False)
    city = sa.Column(sa.String(100), nullable=False)
    postal_code = sa.Column(sa.Integer, nullable=False)
    country = sa.Column(sa.String(100), nullable=False)

    cars = relationship("CustomerCar", back_populates="customer")

    def __repr__(self):
        return f'Customer: {self.customer_id}, {self.first_name}, {self.last_name}, {self.address}, {self.city}, {self.postal_code}, ' \
               f'{self.country}'
