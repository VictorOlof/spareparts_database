from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'

    category_id = sa.Column(sa.Integer, primary_key=True)
    category_name = sa.Column(sa.String(50), nullable=False)
    category_description = sa.Column(sa.String(50), nullable=False)

    # address = relationship("Address", back_populates="customer")

    def __repr__(self):
        return f'Category: {self.category_id}, {self.category_name}, {self.category_description}'
