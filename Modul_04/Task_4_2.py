def check_palindromes(text: str) -> bool:
    """
    Returns 'True' or 'False', based on the argument being palindrome or not:
    Argument:
        text
    """

    for char in text:
        if char in ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ó', 'Ś', 'Ź', 'Ż']:
            pass
        elif ord(char) < 65 or 90 < ord(char) < 97 or 122 < ord(char):
            text = text.replace(char, '')

    text = text.lower()
    text_length = len(text)

    if text_length % 2 == 0:
        for i in range(int(text_length / 2)):
            if text[i] != text[-(i + 1)]:
                return False
    else:
        for i in range(int((text_length - 1) / 2)):
            if text[i] != text[-(i + 1)]:
                return False

    return True


print(check_palindromes("Ejże, trener też je!"))
