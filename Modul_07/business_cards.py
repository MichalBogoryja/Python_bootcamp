from faker import Faker

fake = Faker()
persons = []


class Card:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail

        # Variables
        self._fullname_length = 0

    def __str__(self):
        return f'{self.name} {self.surname} mail: {self.mail}'

    def __repr__(self):
        return f'{self.name} {self.surname} mail: {self.mail}'

    def contact(self):
        print(f'Kontaktuję się z {self.name} {self.surname} {self.position} '
              f'{self.mail}')

    @property
    def fullname_length(self):
        self._fullname_length = len(self.name) + len(self.surname) + 1
        return self._fullname_length


for i in range(5):
    full_name = fake.name()
    full_name = full_name.split(' ', 1)
    if full_name[0].find('.') >= 0:
        full_name = full_name[1:]
        full_name = full_name[0].split(' ', 1)
    person_name = full_name[0]
    person_surname = full_name[1]
    person_company = fake.company()
    person_position = fake.job()
    if person_company.isalnum():
        person_mail = person_name.lower() + '.' + person_surname.lower() \
                      + '@' + person_company.lower() + '.com'
    else:
        company_alnum = ''.join([x for x in person_company if x.isalnum()])
        person_mail = person_name.lower() + '.' + person_surname.lower() \
                      + '@' + company_alnum.lower() + '.com'

    persons.append(Card(name=person_name, surname=person_surname,
                        company=person_company, position=fake.job(),
                        mail=person_mail))


# print(*persons, sep='\n')

by_name = sorted(persons, key=lambda person: person.name)
by_surname = sorted(persons, key=lambda person: person.surname)
by_mail = sorted(persons, key=lambda person: person.mail)

print(*by_surname, sep='\n')

for person in persons:
    person.contact()
    print(person.fullname_length)

