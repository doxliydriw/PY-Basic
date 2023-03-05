def generate_cube_numbers(end):
    """
    Function generates number to the third power from 2 up to limit iset by 'end' variable.
    :param end:
    :return: int
    """
    x = 2
    while x ** 3 <= end:
        yield x ** 3
        x = x + 1
    return


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'поскольку оно меньше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 в кубе это 125, а оно уже больше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 в кубе это 1000'
