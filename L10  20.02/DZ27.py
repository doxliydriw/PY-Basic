def is_even(digit) -> True or False:
    """Function checks whether number is even"""
    x = digit / 2
    res = x.is_integer()
    return res


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')