def first_word(text) -> str:
    import string
    y = (list(string.punctuation))
    y = (y[:6] + y[7:])
    y = set(y)
    string = text.split()
    i = 0
    while i <= len(string):
        x = set(string[i])
        x.difference_update(y)
        if len(list(x)) != 0:
            x = set(string[i])
            a = string[i]
            z = x.copy()
            if x.isdisjoint(y):
                return a
            z = list(z.intersection(y))
            w = z[0]
            b = a.replace(w, ' ')
            a = b.split()
            return a[0]
        i += 1


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word("... and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
