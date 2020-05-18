from business_cards import create_contacts


def test_phone_number_has_correct_length():
    card = create_contacts(1, True)
    phone_number = card[0].phone.replace(" ", "")
    assert 9 <= len(phone_number) <= 12


def test_mail_structure():
    card = create_contacts(1, True)
    mail = card[0].mail
    assert mail.replace(".", "").replace("@", "").isalnum()
