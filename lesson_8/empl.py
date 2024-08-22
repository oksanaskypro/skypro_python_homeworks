import requests


class Company:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        BASE_HEADERS = {
        "x-client-token": self.get_token()
        }
        resp = requests.post(f"{self.url}/company", json=company, headers=BASE_HEADERS)
        if resp.status_code != 201:
            raise Exception(f"Failed to create company: {resp.status_code}")
        return resp.json()

    def get_list_employee(self, company_id):
        params = {"company": company_id}
        resp = requests.get(
            f"{self.url}/employee",
            params=params,
            headers=self.headers  # Добавляем заголовок для аутентификации
        )
        resp.raise_for_status()  # Проверяем успешность запроса
        return resp

    def get_employee_by_id(self, employee_id):
        resp = requests.get(
            f"{self.url}/employee/{employee_id}",
            headers=self.headers  # Добавляем заголовок для аутентификации
        )
        resp.raise_for_status()  # Проверяем успешность запроса
        return resp
    
    def add_new_employee(self, new_id, name, last_name, email="test@test.ru", phone="89999999999", birthdate="2024-08-13T14:05:19.766Z"):
        employee = {
            "firstName": name,
            "lastName": last_name,
            "middleName": "-",
            "companyId": new_id,
            "email": email,
            "url": "string",
            "phone": phone,
            "birthdate": birthdate,
            "isActive": True
        }

        BASE_HEADERS = {
        "x-client-token": self.get_token()
        }
        resp = requests.post(f"{self.url}/employee", headers=BASE_HEADERS, json=employee)
        resp.raise_for_status()  # Проверяем, прошел ли запрос успешно
        return resp  # Возвращаем объект ответа Response
    
    def update_employee_info(self, id_employee, last_name, email):
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": True
        }

        BASE_HEADERS = {
        "x-client-token": self.get_token()
        } 
        resp = requests.patch(f"{self.url}/employee/{id_employee}", headers=BASE_HEADERS, json=user_info)
        resp.raise_for_status()  
        return resp  