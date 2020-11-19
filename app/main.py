from Data.db import Base, engine, session
from Data.models.address import Address
from Data.models.customer import Customer
from UI.main_menu import main_menu


def main():
    Base.metadata.create_all(engine)

    main_menu()

if __name__ == '__main__':
    main()
