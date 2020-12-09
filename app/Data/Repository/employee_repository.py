from Data.db import session
from Data.models.employee import Employee


def create_employee(employee_first_name, employee_last_name, employee_store_id):
    employee = Employee(employee_first_name=employee_first_name, employee_last_name=employee_last_name,
                        employee_store_id=employee_store_id)

    session.add(employee)
    session.commit()
