lst = [0, 1, 0, 1, 0, 0, 0, 1, 0, 2, 3]
lst0 = []
x = 0
y = 0
while x <= lst.count(0) + 1:
    lst0.append(lst.index(0, x))
    x = lst.index(0, x) + 1
x = lst.count(0)
print(lst0)
lst.sort()
del(lst[0:(x)])
print(lst)

# while z <= lst(len):
#     y = lst.index(z)
#     print(lst.index(0))
#
# print(y)
# lst0.append(y)
# print(lst0)