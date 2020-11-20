from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ProductOrder(Base):
    __tablename__ = 'product_orders'

    product_order_id = sa.Column(sa.Integer, primary_key=True)
    quantity_limit = sa.Column(sa.Integer, nullable=False)
    order_amount = sa.Column(sa.Integer, nullable=False)
    order_incoming_date = sa.Column(sa.Date, nullable=False)
    product_order_product_id = sa.Column(sa.Integer, sa.ForeignKey('products_product'),  nullable=False)

    def __repr__(self):
        return f'product_order: {self.product_order_id}, {self.quantity_limit}, {self.order_amount},' \
               f'{self.order_incoming_date}, {self.product_order_product_id}'
