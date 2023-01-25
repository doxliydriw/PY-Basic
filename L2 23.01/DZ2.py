x = input('Input 4 digit number:')
x = int(x)
y = x + 1
left, right = divmod(x, 1000)
y = left * 10
print(left)
left, right = divmod(x, 100)
y = left - y
print(y)
y = left * 10
left, right = divmod(x, 10)
y = left - y
print(y)
y = left * 10
left, right = divmod(x, 1)
y = left - y
print(y)

