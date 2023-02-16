# def correct_sentence(text):
#     pass
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings, friends") == "Greetings, friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')
def correct_sentence(text):
    text = text.replace(text[0], (text[0]).title(), 1)
    if text[-1] != '.':
        text += '.'
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
print('ОК')
