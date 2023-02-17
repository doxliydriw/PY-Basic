import string
text = 'A man, a plan, a canal: Panama'
a = 0
b = -1
text = text.lower()
y = string.punctuation + ' '
for i in text:
    if i in y:
        text = text[:text.find(i)] + text[text.find(i) + 1:]
print(text)
while a < len(text):
    if text[a] != text[b]:
        z = False
        break
    z = True
    a += 1
    b -= 1
print(z)
