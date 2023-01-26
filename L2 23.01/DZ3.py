x = input('Input 5 digit number:')
x = int(x)
left, right = divmod(x, 10)
a = right * 10000
left, right = divmod(left, 10)
a = a + (right * 1000)
left, right = divmod(left, 10)
a = a + (right * 100)
left, right = divmod(left, 10)
a = a + (right * 10)
left, right = divmod(left, 10)
a = a + right
print (a)

