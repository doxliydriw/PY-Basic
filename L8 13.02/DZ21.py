def is_palindrome(text):
    import string
    a = 0
    b = -1
    text = text.lower()
    y = string.punctuation + ' '
    for i in text:
        if i in y:
            text = text[:text.find(i)] + text[text.find(i) + 1:]
    z = True
    while a <= len(text) and b >= -abs(len(text)):
        if text[a] != text[b]:
            z = False
            break
        a += 1
        b -= 1
    return z


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
print("ОК")
