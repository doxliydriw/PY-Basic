def add_one(some_list):
    some_str = "".join([str(y) for y in some_list])
    some_list.clear()
    some_str = str(int(some_str) + 1)
    for i in some_str:
        some_list.append(int(i))
    return(some_list)

# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9, 9]) == [1, 0, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")