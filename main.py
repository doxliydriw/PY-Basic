text = "greetings, friends"
text = text.replace(text[0], (text[0]).title(), 1)
print(text)
if text[-1] != '.':
    text += '.'
print(text)
