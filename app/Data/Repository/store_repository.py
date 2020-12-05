from Data.models.store import Store
from Data.Repository import repo_functions as rf


def create_store(store_name):
    rf.add_model(Store, store_name=store_name)


def list_all_stores():
    return rf.get_all_models(Store)
