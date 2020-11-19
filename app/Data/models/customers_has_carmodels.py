from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CustomerCar(Base):
    __tablename__ = 'customers_has_car_models'

    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), primary_key=True)
    car_models_id = sa.Column(sa.Integer, sa.ForeignKey('car_models.car_model_id'), primary_key=True)
    reg_plate = sa.Column(sa.String(6), primary_key=True, unique=True)
    color = sa.Column(sa.String(50), nullable=False)

    customers = relationship("Customer", back_populates="customers_has_car_models")
    car_models = relationship("CarModel", back_populates="customers_has_car_models")

    def __repr__(self):
        return f'CustomerCar: {self.customer_id}, {self.car_models_id}, {self.reg_plate}, {self.color}'
