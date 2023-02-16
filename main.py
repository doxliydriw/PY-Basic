import random
lst3 = []
lst5 = []
count = random.randint(10, 100)
i = 0
print(count)
while i < count:
    i += 1
    lst_item = random.randint(0, 100)
    print(lst_item % 3, lst_item % 5)
    if lst_item % 3 == 0 and lst_item % 5 == 0:
        lst5.append(lst_item)
        lst3.append(lst_item)
    elif lst_item % 5 == 0:
        lst5.append(lst_item)
    elif lst_item % 3 == 0:
        lst3.append(lst_item)
print(lst3)
print(lst5)
common = (set(lst3)).intersection(set(lst5))
print(common)
