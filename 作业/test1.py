a = int(input())
while a != 1:
    if a % 2 == 0:
        a = a / 2
    else:
        a = a * 3 + 1
    if a != 1:
        print("%d" % a, end=",")
    else:
        print("%d" % a)
