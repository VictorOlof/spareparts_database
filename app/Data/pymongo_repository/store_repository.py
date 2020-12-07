import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def create_store(store_name):
    rf.add_model(mm.Store, store_name=store_name)


def list_all_stores():
    return rf.get_all_models(mm.Store)
