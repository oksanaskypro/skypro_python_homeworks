from smartphone import Smartphone
catalog = []
phone1 = Smartphone ('Samsung', 'Galaxy A54', '+79505485879')
phone2 = Smartphone ('Huawei', 'nova 11 Pro', '+76807455221')
phone3 = Smartphone ('Xiaomi', '13 Pro', '+73457854421')
phone4 = Smartphone ('ASUS', 'Zenfone 10', '+75468529551')
phone5 = Smartphone ('POCO', 'F5 Pro', '+78524567882')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print (f"{phone.marka_sm} - {phone.model_sm}, {phone.number_phone_sm}")