from pymongo import MongoClient
from abc import ABC

client = MongoClient('mongodb://root:soda1ice@localhost:27027')
db = client.carparts_db


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()

        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

        for key in data:
            setattr(self, key, data[key])

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del (self.__dict__['_id'])
            return self.collection.insert_one(self.__dict__)

        else:
            return self.collection.update({'_id': self._id}, self.__dict__)

    def update_field(self, column_value, value):
        return self.collection.update({'_id': self._id}, {"$set": {column_value: value}})

    def remove_doc(self):
        self.collection.delete_one({'_id': self._id})

    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))

    @classmethod
    def delete(cls, **kwargs):
        cls.collection.delete_many(kwargs)

    @classmethod
    def insert_to_embedded_list(cls, obj_id, list_name: str, value: dict):
        cls.collection.update_one({'_id': obj_id}, {'$push': {list_name: value}})

    @classmethod
    def insert_to_embedded_field(cls, obj_id, field_name: str, value: dict):
        cls.collection.update_one({'_id': obj_id}, {'$set': {field_name: value}})

