import Data.pymongo_repository.store_repository as st


def create_store(store_name):
    st.create_store(store_name)


def list_all_stores():
    return st.list_all_stores()
