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

    def __repr__(self):
        return f'{self.order_id}'.ljust(12) + f'{self.order_date}'.ljust(15) + f'{self.required_date}'.ljust(18) + \
               f'{self.shipped_date}'.ljust(20) + f'{self.status}'.ljust(18) + f'{self.comment}'.ljust(15) + \
               f'{self.employee_id}'.ljust(15) + f'{self.customer_id}'.ljust(15)






"""return f'{self.order_id}'.ljust(12) + f'{self.order_date}'.ljust(15) + f'{self.required_date}'.ljust(18) +\
               f'{self.shipped_date}'.ljust(20) + f'{self.status}'.ljust(18) + f'{self.comment}'.ljust(15) + \
               f'{self.employee_id}'.ljust(15) + f'{self.customer_id}'.ljust(15)"""


"""return f'   {self.order_id}        {self.order_date}     {self.required_date}     ' \
                               f'{self.shipped_date}     {self.status}        {self.comment}            ' \
                               f'{self.employee_id}              {self.customer_id}'"""
