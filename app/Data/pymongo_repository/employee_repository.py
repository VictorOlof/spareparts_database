import Data.pymongo_models as mm
from Data.pymongo_repository import repo_functions as rf


def create_employee(employee_first_name, employee_last_name, employee_store_id):
    rf.add_model(mm.Employee, employee_first_name=employee_first_name, employee_last_name=employee_last_name,
                 employee_store_id=employee_store_id)


def get_all_employees():
    return rf.get_all_models(mm.Employee)
