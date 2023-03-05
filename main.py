end = 3
i = 2
while i <= end:
    for x in range(2, int(i ** 0.5 + 1)):
        if i % x == 0:
            break
    else:
        print(i)
    i += 1