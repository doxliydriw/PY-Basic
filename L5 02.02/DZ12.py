# 'I like python community!' -> #ILikePythonCommunity
import string
y = string.punctuation
y = list(y)
y1 = ' '
x = input('Input string:')
for i in x:
    if i in y:
        x = x[:x.index(i)] + x[(x.index(i)+1):]
x = '#' + x.title()
for i in x:
    if i in y1:
        x = x[:x.index(i)] + x[(x.index(i)+1):]
x1 = list(x)
if len(x1) > 140:
    x = x[:140]
print(x)
