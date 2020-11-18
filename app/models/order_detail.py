from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    __tablename__ = 'order_details'

    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.product_id'), primary_key=True, nullable=False)
    quantity_ordered = sa.Column(sa.Integer, nullable=False)
    sell_price_each = sa.Column(sa.Float(50), nullable=False)
    order_line_number = sa.Column(sa.Integer, nullable=False, unique=True)

    # address = relationship("Address", back_populates="customer")

    def __repr__(self):
        return f'Order details: {self.order_id}, {self.product_id}, {self.quantity_ordered}, {self.sell_price_each},' \
               f' {self.order_line_number}'
