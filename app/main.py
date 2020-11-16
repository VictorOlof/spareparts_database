from db import Base, engine, session
from models.customers import Customer
from models.orders import Order
from models.parents import Parent
from models.children import Child


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
