from lesson_9.empl import Company
from lesson_9.EmplTable import EmplTable
import pytest

api = Company("https://x-clients-be.onrender.com")
db = EmplTable("postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def setup_module(module):
    db.create_table()
    db.delete_all_employees()  # Очищаем таблицу сотрудников перед тестами

def teardown_module(module):
    db.dispose()  # Используем метод dispose()

def test_create_and_get_employee():
    name = "SkyPro"
    descr = "testing"
    company = api.create_company(name, descr)
    new_company_id = company["id"]

    len_before = len(db.get_employees())

    new_employee_id = db.insert_employee("Mike", "Sorreto", "+123456789", new_company_id).inserted_primary_key[0]

    len_after = len(db.get_employees())

    assert len_after - len_before == 1

    employee_list = api.get_list_employee(new_company_id)
    assert any(employee["firstName"] == "Mike" and employee["lastName"] == "Sorreto" for employee in employee_list)

def test_update_employee():
    employees = db.get_employees()
    assert len(employees) > 0

    employee_id = employees[0]["id"]
    db.update_employee(employee_id, "Jane", "Doe", "Middle", "+987654321", "jane.doe@example.com", "http://example.com")

    updated_employee = db.get_employee_by_id(employee_id)  # Получаем обновленного сотрудника напрямую
    assert updated_employee["first_name"] == "Jane"
    assert updated_employee["last_name"] == "Doe"
    assert updated_employee["middle_name"] == "Middle"
    assert updated_employee["phone"] == "+987654321"
    assert updated_employee["email"] == "jane.doe@example.com"
    assert updated_employee["avatar_url"] == "http://example.com"
    assert updated_employee["is_active"] == True  # Это поле не должно измениться
def test_delete_all_employees():
    employees = db.get_employees()

    for employee in employees:
        employee_id = employee["id"]
        db.delete_employee(employee_id)

    employees_after_deletion = db.get_employees()
    assert len(employees_after_deletion) == 0