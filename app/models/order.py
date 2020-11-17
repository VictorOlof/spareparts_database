from db import Base
import sqlalchemy as sa

class Order(Base):
    __tablename__ = 'orders'

    order_id = sa.Column(sa.Integer, primary_key=True)
    order_date = sa.Column(sa.Date)
    required_date = sa.Column(sa.Date)
    shipped_date = sa.Column(sa.Date)
    status = sa.Column(sa.String(50))
    comment = sa.Column(sa.String(50))
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.employee_id'))
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'))
