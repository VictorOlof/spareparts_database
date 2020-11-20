from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ProductCar(Base):
    __tablename__ = 'products_has_car_models'

    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.product_id'), primary_key=True)
    car_model_id = sa.Column(sa.Integer, sa.ForeignKey('car_models.car_model_id'), primary_key=True)

    # products = relationship("Product", back_populates="products_has_car_models")
    # car_models = relationship("CarModel", back_populates="products_has_car_models")

    def __repr__(self):
        return f'CustomerCar: {self.product_id}, {self.car_model_id}'
