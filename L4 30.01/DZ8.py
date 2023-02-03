# [1, 3, 5] => 30
lst = [1, 3, 5]
# [6] => 36
# lst = [6]
# [] => 0
# lst = []
x = 0
i = 0
if len(lst) != 0:
    while lst:
        x = x + lst[i]
        i = i + 2
        if i > len(lst):
            break
    x = x * lst[-1]
else:
    x = 0
print('result', x)
