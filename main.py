import keyword
import string
x = input('Input User name:')
y = string.punctuation
y = list(y) + [' ']
z = 0
del(y[26])
for i in x:
    if i.isupper():
        print('False')
        break
    elif i in y:
        print('False')
        break
    elif keyword.iskeyword(x):
        print('False')
        break
    elif (x[0]).isdigit():
        print('False')
        break
    else:
        z = z + 1
        if z == len(x):
            print('True')
