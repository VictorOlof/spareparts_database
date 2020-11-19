from db import Base
import sqlalchemy as sa

class Order(Base):
    __tablename__ = 'orders'

    order_id = sa.Column(sa.Integer, primary_key=True)
    order_date = sa.Column(sa.Date, nullable=False)
    required_date = sa.Column(sa.Date, nullable=False)
    shipped_date = sa.Column(sa.Date, nullable=False)
    status = sa.Column(sa.String(50), nullable=False)
    comment = sa.Column(sa.String(50))
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.employee_id'), nullable=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), nullable=False)
