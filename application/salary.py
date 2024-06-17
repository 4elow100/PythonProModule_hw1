from application.db.people import get_employees


def calculate_salary(id_employee):
    id_employees = get_employees()
    if id_employee in id_employees:
        employee_salary = 50000
        salary = 50000 * 1.2 + 9500
        return salary
    else:
        return 0
