def is_even(digit) -> True or False:
    """Function checks whether number is even"""
    x = int(str(digit)[-1])
    lst = [i for i in range(0, x + 1, 2)]
    return x in lst


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
