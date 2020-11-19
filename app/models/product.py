from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'product'

    product_id = sa.Column(sa.Integer, primary_key=True)
    product_name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.String(200))
    quantity_in_stock = sa.Column(sa.Integer, nullable=False)
    storage_space = sa.Column(sa.String, nullable=False)
    buy_price = sa.Column(sa.Float(50), nullable=False)
    products_supplier_id = sa.Column(sa.Integer, sa.ForeignKey('supplier.supplier_id'), nullable=False)
    category_category_id = sa.Column(sa.Integer, sa.ForeignKey('category.categories_id'), nullable=False)
    manufacturer_manufacturer_id = sa.Column(sa.Integer, sa.ForeignKey('manufacturers.manufacturers_id'), nullable=False)

    def __repr__(self):
        return f'Products: {self.product_id}, {self.product_name}, {self.description}, {self.quantity_in_stock},' \
               f'{self.storage_space}, {self.buy_price}, {self.products_supplier_id}, {self.category_category_id}' \
               f'{self.manufacturer_manufacturer_id}'
