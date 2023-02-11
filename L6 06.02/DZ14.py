x = input('Input number:')
res = 1
if int(x) > 0:
    while True:
        for i in x:
            res *= int(i)
        if res <= 9:
            print(res)
            break
        else:
            x = str(res)
            res = 1
