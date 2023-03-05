def difference(*args) -> int:
    """Function calculates difference between minimum amd maximum number in set of numbers"""
    nmbr_set = list(args)
    if len(nmbr_set) == 0:
        return 0
    else:
        maxnmbr = nmbr_set[0]
        minnmbr = nmbr_set[0]
        for i in nmbr_set:
            if i > maxnmbr:
                maxnmbr = i
            elif i < minnmbr:
                minnmbr = i
    return round((maxnmbr - minnmbr), 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference (5, -5) == 10, 'Test2'
assert difference (10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference () == 0, 'Test4'
print('OK')

