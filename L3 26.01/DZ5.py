# TO DO lst = [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
lst = [1, 2, 3, 4, 5, 6]
# TO DO lst = [1, 2, 3] => [[1, 2], [3]]
# lst = [1, 2, 3]
# TO DO lst = [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# lst = [1, 2, 3, 4, 5]
# TO DO lst = [1] => [[1], []]
# lst = [1]
# TO DO lst = [] => [[], []]
# lst = []
if len(lst) == 0:
    # print(len(lst))
    lst1 = ([lst]*2)
    # print(len(lst1))
    print('Empty list', lst1)
elif len(lst) == 1:
    # print(len(lst))
    lst1 = (lst, [])
    # print(len(lst1))
    print('One element list', lst1)
elif (len(lst)/2).is_integer():
    # print(len(lst))
    lst1 = ([(lst[0:(len(lst) // 2)])], [(lst[(len(lst) // 2):])])
    # print(len(lst1))
    print('Even list', lst1)
else:
    # print(len(lst))
    lst1 = ([lst[:((len(lst)//2)+1)]] + [lst[((len(lst)//2)+1):]])
    # print(len(lst1))
    print('Not even list', lst1)
print('End')
