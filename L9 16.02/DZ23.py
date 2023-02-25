def popular_words (text, findlst) -> dict:
    '''Function which gets the list of strings, calculates how many times each string is found in given sentance and
    generates the dictionary where keys are the srtings from the list and values are number strings found in sentance'''
    dict_one = {}
    for i in findlst:
        dict_one[i] = text.lower().split().count(i)
        print(dict_one)
    return(dict_one)


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
print('OK')