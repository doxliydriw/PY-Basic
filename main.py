text = 'When I was One I had just begun When I was Two I was nearly new'
count = {}
findlst = ['i', 'was', 'three', 'near']
textlst = text.lower().split()
print(textlst)
v = 0
for i in findlst:
    for i in textlst:
        textlst[v] == i:
        v += 1
        count[i] = count.get(i, 0) + 1
        print(count)
    v +=1

