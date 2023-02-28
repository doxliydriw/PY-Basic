def exponent(value):
    """Function returns 'value' to the power of '2'"""
    return value ** 2


def count(start, end, func):
    """Generator of set based on 'func' logic  defined by user returns values staring
         from 'start' position up to 'end' position in set defined by user"""
    for i in range(end):
        i += 1
        yield start
        start = func(start)


print(list(count(2, 7, exponent)))
