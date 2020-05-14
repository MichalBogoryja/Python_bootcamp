from faker import Faker
from datetime import datetime

fake = Faker()
persons = []


class BaseCard:
    def __init__(self, name, surname, phone, mail):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.mail = mail

        # Variables
        self._fullname_length = 0

    def __str__(self):
        return f'{self.name} {self.surname} mail: {self.mail}'

    def __repr__(self):
        return f'{self.name} {self.surname} mail: {self.mail}'

    def contact(self):
        print(f'\nWybieram numer {self.phone} i dzwonię do {self.name} '
              f'{self.surname}', end='')

    @property
    def fullname_length(self):
        self._fullname_length = len(self.name) + len(self.surname) + 1
        return self._fullname_length


class BusinessCard(BaseCard):
    def __init__(self, company, position, business_phone, business_mail,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone
        self.business_mail = business_mail

    def __str__(self):
        return f'{self.name} {self.surname} b_mail: {self.business_mail}'

    def __repr__(self):
        return f'{self.name} {self.surname} b_mail: {self.business_mail}'

    def contact(self, *args, **kwargs):
        super().contact(*args, **kwargs)
        print(f' lub dzwonię na numer firmowy {self.business_phone}', end='')


def generate_basic_info():
    data = {}

    full_name = fake.name()
    full_name = full_name.split(' ', 1)
    if full_name[0].find('.') >= 0:
        full_name = full_name[1:]
        full_name = full_name[0].split(' ', 1)
    data['name'] = full_name[0]
    data['surname'] = full_name[1]
    data['phone'] = fake.phone_number()
    data['mail'] = fake.free_email()

    return data


def generate_business_info(person_info):
    data = {}

    data['company'] = fake.company()
    data['position'] = fake.job()
    data['phone'] = fake.phone_number()

    if data['company'].isalnum():
        mail = person_info['name'].lower() + '.' \
                      + person_info['surname'].lower() + '@' \
                      + data['company'].lower() + '.com'
    else:
        company_alnum = ''.join([x for x in data['company'] if x.isalnum()])
        mail = person_info['name'].lower() + '.' \
                      + person_info['surname'].lower() \
                      + '@' + company_alnum.lower() + '.com'

    data['mail'] = mail

    return data


def time_count(func):

    def wrapper(x, y):
        start_time = datetime.now()

        result = func(x, y)

        end_time = datetime.now()
        time_needed = end_time - start_time
        print(f'Time needed: {time_needed.seconds}.'
              f'{time_needed.microseconds}s')
        return result

    return wrapper


@time_count
def create_contacts(amount, private):
    for i in range(amount):
        new_person = generate_basic_info()
        if private:
            persons.append(BaseCard(name=new_person['name'],
                                    surname=new_person['surname'],
                                    phone=new_person['phone'],
                                    mail=new_person['mail']))
        else:
            new_b_person = generate_business_info(new_person)
            persons.append(BusinessCard(name=new_person['name'],
                                        surname=new_person['surname'],
                                        phone=new_person['phone'],
                                        mail=new_person['mail'],
                                        company=new_b_person['company'],
                                        position=new_b_person['position'],
                                        business_phone=new_b_person['phone'],
                                        business_mail=new_b_person['mail']))


create_contacts(5, True)
create_contacts(15, False)

print('')
print(*persons, sep='\n')

by_name = sorted(persons, key=lambda person: person.name)
by_surname = sorted(persons, key=lambda person: person.surname)
by_mail = sorted(persons, key=lambda person: person.mail)

print(*by_surname, sep='\n')

for person in by_surname:
    person.contact()
    print(f'''
Length of the person's name and surname is: {person.fullname_length}''')
