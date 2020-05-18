from business_cards import create_contacts


def test_phone():
    card = create_contacts(1, True)
    phone_number = card[0].phone.replace(" ", "")
    assert 9 <= len(phone_number) <= 12
