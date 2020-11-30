from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Store(Base):
    __tablename__ = 'stores'

    store_id = sa.Column(sa.Integer, primary_key=True)
    store_name = sa.Column(sa.String(50), nullable=False)

    employees = relationship("Employee", back_populates="store")

    def __repr__(self):
        return '{:15}{}'.format(str(self.store_id), str(self.store_name))

