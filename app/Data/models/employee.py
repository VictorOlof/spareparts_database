from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = sa.Column(sa.Integer, primary_key=True)
    employee_first_name = sa.Column(sa.String(50), nullable=False)
    employee_last_name = sa.Column(sa.String(50), nullable=False)
    employee_store_id = sa.Column(sa.Integer, sa.ForeignKey('stores.store_id'), nullable=False)

    orders = relationship("Order", back_populates="employee")
    store = relationship("Store", back_populates="employees")

    def __repr__(self):
        return f'employee: {self.employee_first_name}, {self.employee_last_name}, {self.employee_store_id}'

