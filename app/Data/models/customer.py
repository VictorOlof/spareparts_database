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
    company_name = sa.Column(sa.String(100), nullable=True)
    org_number = sa.Column(sa.String(100), nullable=True)

    cars = relationship("CustomerCar", back_populates="customer", cascade="all, delete")
    orders = relationship("Order", back_populates="customer", cascade="all, delete")

    def __repr__(self):
        return f'Customer: {self.customer_id}, {self.first_name}, {self.last_name}, {self.address}, {self.city}, ' \
               f'{self.postal_code}, {self.country}'
