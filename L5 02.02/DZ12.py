# 'I like python community!' -> #ILikePythonCommunity
import string
y = string.punctuation
y = list(y)
x = input('Input string:')
for i in x:
    x = x.replace("i", "")
x = '#' + (x.title()).replace(" ", "")
x1 = list(x)
if len(x1) > 140:
    x = x[:140]
print(x)
