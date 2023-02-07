a = ['yes', 'YES', 'Yes', 'Y', 'y']
b = ('y')
while b in a:
    x = float(input('Type 1st number:'))
    z = input('Indicate action (+,-,*,/):')
    y = float(input('Type 2nd number:'))
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
    b = input('Another operation? Y/N')
print('The end')
