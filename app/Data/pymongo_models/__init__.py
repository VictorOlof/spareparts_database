from Data.base_document import Document, db


class Store(Document):
    collection = db.stores

    def __repr__(self):
        return f"Customer = {self.__dict__}"


class Employee(Document):
    collection = db.employees

    def __repr__(self):
        return f"Employee = {self.__dict__}"


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

