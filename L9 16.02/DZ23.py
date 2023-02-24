def popular_words (text, lst) ->
    '''Function which gets the list of strings, calculates how many times each string is found in given sentance and
    generates the dictionary where valueas are the srtings from the list and keys are number strings found in sentance'''


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
print('OK')