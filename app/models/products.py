from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'

    products_id = sa.Column(sa.Integer, primary_key=True)
    products_name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.String(200))
    quantity_in_stock = sa.Column(sa.Integer, nullable=False)
    storage_space = sa.Column(sa.String, nullable=False)
    buy_price = sa.Column(sa.Float(50), nullable=False)
    supplier_supplier_id = sa.Column(sa.Integer, nullable=False)
    category_category_id = sa.Column(sa.Integer, nullable=False)
    manufacturer_manufacturer_id = sa.Column(sa.Integer, nullable=False)

    def __repr__(self):
        return f'Products: {self.products_id}, {self.products_name}, {self.description}, {self.quantity_in_stock},' \
               f'{self.storage_space}, {self.buy_price}, {self.supplier_supplier_id}, {self.category_category_id}' \
               f'{self.manufacturer_manufacturer_id}'
