from business_cards import create_contacts, generate_business_info


def test_phone_number_has_correct_length():
    card = create_contacts(1, True)
    phone_number = card[0].phone.replace(" ", "")
    assert 9 <= len(phone_number) <= 12


def test_phone_is_a_number():
    card = create_contacts(1, True)
    phone_number = card[0].phone.replace(" ", "").replace("+", "00")
    assert phone_number.isnumeric()


def test_mail_structure():
    card = create_contacts(1, True)
    mail = card[0].mail
    assert mail.replace(".", "").replace("@", "").isalnum()
    assert (''.join(mail.split('.')[-1:]) == 'pl' or
            ''.join(mail.split('.')[-1:]) == 'com')


def test_company_name():
    card = create_contacts(1, False)
    company_name = card[0].company
    assert company_name.isalnum()
