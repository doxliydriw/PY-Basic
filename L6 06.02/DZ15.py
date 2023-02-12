# 1 minute = 60 sec, i hour = 60*60, 1 day = 60*60*24
x = int(input('Input number from 1 to 8639999:'))
if x in range(0, 8639999):
    days, div = divmod(x, 86400)
    # print(type(days))
    my_tuple = divmod(x, 86400)
    # print(my_tuple)
    z = my_tuple[0]
    print(type(z))
    print(days)
    hours, div = divmod(div, 3600)
    print(hours)
    minutes, div = divmod(div, 60)
    sec = div
    print(days, 'days', hours, 'hours', minutes, 'minutes', sec, 'sec')
    # y = int(tuple[1])
    # print(type(y))
    # my_tuple1 = divmod((tuple[1]), 3600)
    # print(my_tuple)
