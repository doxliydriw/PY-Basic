x = input('Input 5 digit number:')
x = int(x)
left, right = divmod(x, 10)
a = right
print(a)
left, right = divmod(x, 100)
b = right
print (b)
left, right = divmod(b, 10)
b = left
print(b)
print (b,a)
left, right = divmod(x, 1000)
c = right
print(c)
left, right = divmod(x, 10000)
d = right
print(d)
z = a + b + c + d
print(type(z))
int(z)
print(type(z))
print (z)
