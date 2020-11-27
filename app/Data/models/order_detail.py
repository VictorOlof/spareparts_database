from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    __tablename__ = 'order_details'

    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.product_id'), primary_key=True, nullable=False)
    quantity_ordered = sa.Column(sa.Integer, nullable=False)
    sell_price_each = sa.Column(sa.Float(50), nullable=False)

    # address = relationship("Address", back_populates=2"customer")

    def __repr__(self):
        return '{:12}{:15}{:15}{}'.format(str(self.order_id), str(self.product_id),
                                          str(self.quantity_ordered), str(self.sell_price_each))
