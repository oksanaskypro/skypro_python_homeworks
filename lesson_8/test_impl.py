from empl import Company
import pytest

@pytest.fixture(scope="module")
def api():
    return Company("https://x-clients-be.onrender.com")

def test_get_list_of_employees(company):
    name = "Oksana"
    descr = "test"
    return api.create_company(name, descr)
    new_id = company["id"]
    response = api.get_list_employee(new_id)
    employee_list = response.json()
    assert len(employee_list) == 0

    
def test_add_new_employee(api, company):
    name = "Oksana"
    descr = "test"
    return api.create_company(name, descr)
    new_id = company["id"]
    response = api.add_new_employee(new_id, "Oksana1971", "B")
    assert response.status_code == 201  # Проверка статус-кода
    new_employee = response.json()  # Получение данных из JSON
    assert new_employee["id"] > 0
    

def test_get_employee_by_id(company):
    name = "Oksana"
    descr = "test"
    return api.create_company(name, descr)
    new_id = company["id"]
    response = api.add_new_employee(new_id, "Oksana1971", "Be")
    new_employee = response.json()
    id_employee = new_employee["id"]
    assert id_employee.status_code == 201


    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Oksana1971"
    assert get_info["lastName"] == "Be"
    
def test_change_employee_info(company):
    name = "Oksana"
    descr = "test"
    return api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Oksana1971", "Ber")
    id_employee = new_employee["id"]
    assert id_employee.status_code ==201
    
    update = api.update_employee_info(id_employee, "Ber2", "test2@mail.ru")
    assert update["id"] == id_employee
    assert update["email"] == "test2@mail.ru"
    assert update["isActive"] == True


def test_add_employee_without_first_name(company):
    new_id = company["id"]
    with pytest.raises(Exception):
        api.add_new_employee(new_id, "", "LastName")  # Пустое имя

def test_add_employee_without_last_name(company):
    new_id = company["id"]
    with pytest.raises(Exception):
        api.add_new_employee(new_id, "FirstName", "")  # Пустая фамилия

def test_add_employee_without_company_id():
    with pytest.raises(Exception):
        api.add_new_employee(None, "FirstName", "LastName")  # Отсутствует ID компании          