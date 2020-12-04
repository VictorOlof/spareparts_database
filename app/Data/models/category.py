from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'

    category_id = sa.Column(sa.Integer, primary_key=True)
    category_name = sa.Column(sa.String(50), nullable=False)
    category_description = sa.Column(sa.String(50), nullable=False)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f'{self.category_id}, {self.category_name}, {self.category_description}'
