# 'I like python community!' -> #ILikePythonCommunity
import string
y = list(string.punctuation)
x = input('Input string:')
for i in y:
    x = x.replace(i, "")
x = '#' + (x.title()).replace(" ", "")
if len(x) > 140:
    x = x[:140]
print(x)
print(len(x))
