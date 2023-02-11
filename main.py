num = input("enter a number")
n = int(num)
product = 1
for i in num:
    while n != 0:
        rem = n % 10
        product = product * rem
        n = n // 10
        print(product)
    if product >= 9:
        n = product
        product = 1
        num = n
        continue
print(product)
range
