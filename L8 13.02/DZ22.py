def find_unique_value(some_list):
    dict1 = {}
    for i in some_list:
        dict1[i] = dict1.get(i, 0) + 1
    print(dict1)
    dict2 = dict1.copy()
    for i in dict1:
        a = dict2.popitem()
        if a[-1] == 1:
            z = a[0]
    return z

# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")