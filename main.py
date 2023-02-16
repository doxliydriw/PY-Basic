some_list = [1, 2, 3, 4]
some_str = "".join([str(y) for y in some_list])
some_list.clear()
some_str = str(int(some_str) + 1)
for i in some_str:
    some_list.append(int(i))
print(some_list)
