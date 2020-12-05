from Data.db import session
from Data.models.employee import Employee
from Data.Repository import repo_functions as rf


def create_employee(employee_name, employee_store_id):
    rf.add_model(Employee, employee_name=employee_name, employee_store_id=employee_store_id)
