from address import Address
from mailing import Mailing

to_address = Address ('423520', 'Нижнекамск','Нефтяников','65','56')
from_address = Address('155800', 'Кинешма', 'Ленина', '34', '1')
mailing = Mailing (to_address, from_address, 123456, 'ABC123' )

print (f"Отправление {mailing.track_} из {mailing.from_addres.index},{mailing.from_addres.city},{mailing.from_addres.street},{mailing.from_addres.home} - {mailing.from_addres.room}"
       f" в {mailing.to_addres.index},{mailing.to_addres.city},{mailing.to_addres.street}, {mailing.to_addres.home} - {mailing.to_addres.room}."
       f" Стоимость {mailing.cost_} рублей")


