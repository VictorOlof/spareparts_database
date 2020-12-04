from Data.db import session
from Data.models.store import Store


def create_store(store_name):
    store = Store(store_name=store_name)

    session.add(store)
    session.commit()


def list_all_stores():
    return session.query(Store).all()
