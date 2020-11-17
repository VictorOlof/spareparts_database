from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = sa.Column(sa.Integer, primary_key=True)
    supplier_name = sa.Column(sa.String(50), nullable=False)
    supplier_address = sa.Column(sa.String(50), nullable=False)
    supplier_phone = sa.Column(sa.String(50), nullable=False)
    supplier_email = sa.Column(sa.String(50), nullable=False)
    contact_name = sa.Column(sa.String(50))

    # address = relationship("Address", back_populates="customer")

    def __repr__(self):
        return f'Supplier: {self.supplier_id}, {self.supplier_name}, {self.supplier_address}, {self.supplier_phone},' \
               f' {self.supplier_email}, {self.contact_name}'
