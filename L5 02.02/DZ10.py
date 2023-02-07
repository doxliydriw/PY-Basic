import keyword
import string
y = string.punctuation + string.ascii_uppercase
y = list(y) + [' ']
del(y[26])
z = 0
x = input('Input User name:')
for i in x:
    if i in y:
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
