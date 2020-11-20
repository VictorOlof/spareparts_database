from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Store(Base):
    __tablename__ = 'stores'

    store_id = sa.Column(sa.Integer, primary_key=True)
    store_name = sa.Column(sa.String(50), nullable=False)

    def __repr__(self):
        return f'Store: {self.store_id}, {self.store_name}'
