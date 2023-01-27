x = float(input('Type 1st number:'))
z = input('Indicate action (+,-,*,/):')
y = float(input('Input second number:'))
if z == '+':
    print(x, z, y, '=', (x+y))
elif z == '-':
    print(x, z, y, '=', (x-y))
elif z == '*':
    print(x, z, y, '=', (x*y))
elif z == '/' and y != 0:
    print(x, z, y, '=', (x/y))
else:
    print('invalid data')
print('The end')
