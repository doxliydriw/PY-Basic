import random
lst = []
for i in range(random.randint(3, 10)):
    lst.append(random.randint(1, 100))
print(lst)
lst = [lst[0], lst[2], lst[-2]]
print(lst)
