text = 'Hello, hello'
string = 'lo'
y = text.count(string)
if y > 1:
    y = text.find(string) + 1
    y = text.find(string, y)
    print(type(y), y)
