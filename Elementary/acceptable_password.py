from Elementary.functions import is_acceptable_password

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") is False
    assert is_acceptable_password("muchlonger") is True
    assert is_acceptable_password("ashort") is False
    print("Coding complete? Click 'Check' to earn cool rewards!")
