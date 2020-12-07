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


class Product(Document):
    collection = db.products

    def __repr__(self):
        return f"Product = {self.__dict__}"


class Order(Document):
    collection = db.orders

    def __repr__(self):
        return f"Order = {self.__dict__}"


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
