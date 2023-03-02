import string
text = "hi"
a = 0
y = (list(string.punctuation))
print(y)
y = (y[:6]+y[7:])
print(y)
y = set(y)
print(y)
string = text.split()
i = 0
while i <= len(string):
    x = set(string[i])
    # print(x, type(x))
    x.difference_update(y)
    # print(x, 'x')
    if len(list(x)) != 0:
        x = set(string[i])
        a = string[i]
        z = x.copy()
        if x.isdisjoint(y):
            print(a)
            break
        z = list(z.intersection(y))
        # print(str(z[0]), z)
        w = z[0]
        b = a.replace(w, ' ')
        # print(a)
        text = b
        # print(text)
        lst = text.split()
        print(lst[0])
        # print(text[0])
        break
    i += 1

# print(y)
# print(string)
# print((str(x) in y))
# print(x)
