from sqlalchemy import UniqueConstraint
from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CarModel(Base):
    __tablename__ = 'car_models'

    car_model_id = sa.Column(sa.Integer, primary_key=True)
    car_model_name = sa.Column(sa.String(50), nullable=False)
    car_model_year = sa.Column(sa.Integer, nullable=False)
    car_model_car_brand_id = sa.Column(sa.Integer, sa.ForeignKey('car_brands.car_brand_id'), nullable=False)

    __table_args__ = (UniqueConstraint('car_model_name', 'car_model_year', 'car_model_car_brand_id',
                                       name='_model_year_brand_uc'),
                      )

    car_brand = relationship("CarBrand", back_populates="car_models")
    customer_cars = relationship("CustomerCar", back_populates="car_model")
    product_cars = relationship("ProductCar", back_populates="car_model")

    def __repr__(self):
        return f'Car model: {self.car_model_id}, {self.car_model_name}, {self.car_model_year}, ' \
               f'{self.car_model_car_brand_id}'
