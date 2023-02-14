    # 1 minute = 60 sec, i hour = 60*60, 1 day = 60*60*24
    # 0 -> 0 дней, 00:00:00
    # 224930 -> 2 дня, 14:28:50
    # 466289 -> 5 дней, 09:31:29
    # 950400 -> 11 дней, 00:00:00
    # 1209600 -> 14 дней, 00:00:00
    # 8639999 -> 99 дней, 23:59:59
    # 22493 -> 0 дней, 06:14:53
    # # 7948799 -> 91 день, 23:59:59
    # день, (chr(1076)+chr(1077)+chr(1085)+chr(1100))
    # дня, (chr(1076)+chr(1085)+chr(1103))
    # дней, (chr(1076)+chr(1085)+chr(1077)+chr(1081))
x = int(input('Input number from 1 to 8639999:'))
if x in range(8640000):
    days, div = divmod(x, 86400)
    my_tuple = divmod(x, 86400)
    hours, div = divmod(div, 3600)
    minutes, div = divmod(div, 60)
    sec = div
    a = divmod(days, 10)
    if days == 11 or days == 0:
        day1 = (chr(1076) + chr(1085) + chr(1077) + chr(1081))  # дней,
    elif a[-1] == 1 or days == 1:
        day1 = (chr(1076) + chr(1077) + chr(1085) + chr(1100))  # день,
    elif a[-1] == 2 or days == 3 or days == 4:
        day1 = (chr(1076)+chr(1085)+chr(1103)) # дня,
    else:
        day1 = (chr(1076) + chr(1085) + chr(1077) + chr(1081))  # дней,
    print((str(days)).zfill(2), ' ', day1, ' ', (str(hours)).zfill(2), ':',
          (str(minutes)).zfill(2), ':', (str(sec)).zfill(2), sep='')
else:
    print('invalid input')
