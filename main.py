digit = 2494563894038 ** 2
print(digit)
x = int(str(digit)[-1])+1
lst = [i for i in range(0, x, 2)]
print(lst)
x = int(str(digit)[-1])
print(type(x))
print(x in lst)

