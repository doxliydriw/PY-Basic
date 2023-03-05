def prime_generator(end):
    """
    Function will return successively prime numbers from 2 up to number not greater than "end"
    variable.
    :param end: limit for subsequence of generated prime numbers
    :return: prime number
    """
    i = 2
    while i <= end:
        for x in range(2, int(i ** 0.5 + 1)):
            if i % x == 0:
                break
        else:
            yield i
        i += 1


assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(30)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
