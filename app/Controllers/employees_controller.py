import Data.pymongo_repository.employee_repository as p_em


def create_employee(employee_first_name, employee_last_name, employee_store_id):
    p_em.create_employee(employee_first_name, employee_last_name, employee_store_id)


def get_all_employees():
    return p_em.get_all_employees()
