from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CarBrand(Base):
    __tablename__ = 'car_brands'

    car_brand_id = sa.Column(sa.Integer, primary_key=True)
    car_brand_name = sa.Column(sa.String(50), nullable=False, unique=True)

    car_models = relationship("CarModel", back_populates="car_brands")

    def __repr__(self):
        return f'Car model: {self.car_brand_id}, {self.car_brand_name}'
