from sqlalchemy.orm import relationship

from Data.db import Base
import sqlalchemy as sa


class Order(Base):
    __tablename__ = 'orders'

    order_id = sa.Column(sa.Integer, nullable=False, primary_key=True)
    order_date = sa.Column(sa.Date, nullable=False)
    required_date = sa.Column(sa.Date, nullable=False)
    shipped_date = sa.Column(sa.Date, nullable=False)
    status = sa.Column(sa.String(50), nullable=False)
    comment = sa.Column(sa.String(50))
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.employee_id'), nullable=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), nullable=False)

    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    employee = relationship("Employee", back_populates="orders")

    def __repr__(self):
        return f'Order: {self.order_id}, {self.order_date}, {self.required_date}, {self.shipped_date}, {self.status},' \
               f'{self.comment}, {self.employee_id}, {self.customer_id}'
