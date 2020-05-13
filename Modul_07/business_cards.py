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

for person in persons:
    print(person.name + ' ' + person.surname + ' ' + person.mail)