from Data.db import Base, engine, session
from Data.models.supplier import Supplier
from Data.models.category import Category
from Data.models.manufacturer import Manufacturer
from Data.models.car_brand import CarBrand
from Data.models.store import Store
from Data.models.employee import Employee
from Data.models.customer import Customer
from Data.models.car_model import CarModel
from Data.models.customers_has_carmodels import CustomerCar
from Data.models.order import Order
from Data.models.product import Product
from Data.models.products_has_carmodels import ProductCar
from Data.models.order_detail import OrderDetail


from UI.main_menu import main_menu


def main():
    Base.metadata.create_all(engine)

    main_menu()

if __name__ == '__main__':
    main()
