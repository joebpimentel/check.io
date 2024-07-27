def mult_two(a, b):
    # your code here
    return a * b


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    return text.split()[0]


def is_acceptable_password(password: str) -> bool:
    # your code here
    password_length = password.__len__()
    return password_length > 6;


def reverse(text: str) -> str:
    result = ""
    for letter in text:
        result = letter + result
    return result
