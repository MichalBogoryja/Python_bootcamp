def check_palindromes(word: str) -> bool:
    """
    Returns 'True' or 'False', based the argument being palindrome or not:
    Argument:
        word
    """

    text_length = len(word)
    if text_length % 2 == 0:
        print(1)
        return False

    for i in range(int((text_length - 1) / 2)):
        if word[i] != word[-(i+1)]:
            return False

    return True


print(check_palindromes("kajak"))
