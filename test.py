def su(i):
    if i % 2 == 0:
        return 0
    else:
        return 1


a = int(input())
if su(a) == 0:
    print(f"{a}是偶数")
else:
    print(f"{a}不是偶数")
