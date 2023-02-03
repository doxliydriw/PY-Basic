# [1, 3, 5] => 30
# lst = [1, 3, 5]
# [6] => 36
lst = [6]
# [] => 0
# lst = []
x = lst[0]
i = 0
if len(lst) > 0:
    while i <= len(lst)-1:
        i = i + 1
        if not i % 2 == 0:
            continue
        x = x + lst[i]
x = x * lst[i]
print('result', x, '*', lst.pop(), x)
