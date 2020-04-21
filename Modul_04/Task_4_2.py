def check_palindromes(text: str) -> bool:
    """
    Returns 'True' or 'False', based on the argument being palindrome or not:
    Argument:
        text
    """

    text = text.replace(' ', '').lower()
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


print(check_palindromes("Akta generała ma mała renegatka"))
