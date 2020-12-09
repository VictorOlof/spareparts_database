from Data.base_document import Document, db


class Store(Document):
    collection = db.stores

    def __repr__(self):
        return f"Store = {self.__dict__}"

    @property
    def store_id(self):
        return str(self._id)


class OrderDetail(Document):
    collection = db.stores

    def __repr__(self):
        return f"OrderDetail = {self.__dict__}"

    @property
    def order_id(self):
        return str(self._id)


class Employee(Document):
    collection = db.employees

    def __repr__(self):
        return f"Employee = {self.__dict__}"

    @property
    def employee_id(self):
        return str(self._id)


class Customer(Document):
    collection = db.customers

    def __repr__(self):
        return f"Customer = {self.__dict__}"

    @property
    def customer_id(self):
        return str(self._id)


class Product(Document):
    collection = db.products

    def __repr__(self):
        return f"Product = {self.__dict__}"

    @property
    def product_id(self):
        return str(self._id)


class Order(Document):
    collection = db.orders

    def __repr__(self):
        return f"Order = {self.__dict__}"

    @property
    def order_id(self):
        return str(self._id)


class CustomerCar(Document):
    collection = db.customer_cars

    def __repr__(self):
        return f"CustomerCar = {self.__dict__}"


class Category(Document):
    collection = db.categories

    def __repr__(self):
        return f"Category = {self.__dict__}"


class Supplier(Document):
    collection = db.suppliers

    def __repr__(self):
        return f"Supplier = {self.__dict__}"


class Manufacturer(Document):
    collection = db.manufacturers

    def __repr__(self):
        return f"Manufacturer = {self.__dict__}"


def ProductCar():
    return None