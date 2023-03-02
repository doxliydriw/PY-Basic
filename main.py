text = "... don't .touch ,,.it"
w = ','
z = '.'
while w in text:
    text = text.replace(w, ' ')
while z in text:
    text = text.replace(z, ' ')
text = text.split()
print(text[0])
