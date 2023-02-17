dict1 = {}
some_list = [5, 5, 5, 2, 2, 0.5]
for i in some_list:
    dict1[i] = dict1.get(i, 0) + 1
print(dict1)
dict2 = dict1.copy()
for i in dict1:
    a = dict2.popitem()
    if a[-1] == 1:
        z = a[0]
print(z)
print(type(z))
