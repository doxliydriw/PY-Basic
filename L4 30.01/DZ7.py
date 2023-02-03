# [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
lst = [0, 1, 0, 3, 12]
# [0] -> [0]
# lst = [0]
# [1, 0, 3, 0, 0, 0, 5] -> [1, 3, 5, 0, 0, 0, 0]
# lst = [1, 0, 3, 0, 0, 0, 5]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# lst = [1, 2, 3]
x = 0  # the element we sort to the end of the list.
y = 0  # found element counter
if lst.count(x) > 1:
    while lst.count(0)-y > 0:
        lst.pop(lst.index(x))
        lst.append(x)
        y = y + 1
    else:
        print(lst)
print(x, 'count is:', lst.count(x))
