def end_zeros(num: int) -> int:
    # your code here
    int_str: str = num.__str__();
    zeroes_at_end = 0
    for digit in int_str:
        if digit == '0':
            zeroes_at_end += 1
        else:
            zeroes_at_end = 0
    return zeroes_at_end


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
