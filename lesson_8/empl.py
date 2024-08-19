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

    def get_list_employee(self, id):
        my_params = {
            "company": id
        }
        resp = requests.get(f"{self.url}/employee", params=my_params)
        if resp.status_code != 200:
            raise Exception(f"Failed to list employee: {resp.status_code}") 
        return resp.json()

    def get_employee_by_id(self, id_employee):
        resp = requests.get(f"{self.url}/employee/{id_employee}")
        if resp.status_code != 200:
            raise Exception(f"Failed to employee by id: {resp.status_code}")
        return resp.json()

    def add_new_employee(self, new_id, name, last_name, email="test@test.ru", phone="89999999999", birthdate="2024-08-13T14:05:19.766Z"):
        employee = {
        "id": 1,
        "firstName": name,
        "lastName": last_name,
        "middleName": "-",
        "companyId": new_id,
        "email": email,
        "url": "string",
        "phone": phone,
        "birthdate": birthdate,
        "isActive": 'true'
    }

        BASE_HEADERS = {
        "x-client-token": self.get_token()
        }
        resp = requests.post(f"{self.url}/employee", headers=BASE_HEADERS, json=employee)
        if resp.status_code != 201:
            raise Exception(f"Failed to add new employee: {resp.status_code}") 
        return resp.json()
    
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
        if resp.status_code != 200:
            raise Exception(f"Failed to update employee info: {resp.status_code}")
        return resp.json()