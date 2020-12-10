import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def create_employee(employee_first_name, employee_last_name, employee_store_id):
    obj_temp = rf.add_model(mm.Employee, employee_first_name=employee_first_name, employee_last_name=employee_last_name,
                            employee_store_id=employee_store_id)
    add_employee_id_to_stores(obj_temp.employee_id, employee_store_id)


def get_all_employees():
    return rf.get_all_models(mm.Employee)


def add_employee_id_to_stores(employee_id, store_id):
    rf.insert_items_to_embedded_list(mm.Store, store_id, "employees", employee_id)
