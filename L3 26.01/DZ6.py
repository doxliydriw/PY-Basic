# [12, 3, 4, 10] => [10, 12, 3, 4]
lst = [12, 3, 4, 10]
# [1] => [1]
# lst = [1]
# [] => []
# lst = []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
# lst = [12, 3, 4, 10, 8]
if len(lst) == 0:
    # print(len(lst))
    print('Empty list', lst)
elif len(lst) == 1:
    # print(len(lst))
    print('One element list', lst)
else:
    x = lst.pop()
    lst.insert(0, x)
    print(lst)
print('End')
