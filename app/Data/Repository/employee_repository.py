from Data.db import session
from Data.models.employee import Employee


def create_employee(employee_name, employee_store_id):
    employee = Employee(employee_name=employee_name, employee_store_id=employee_store_id)

    session.add(employee)
    session.commit()
