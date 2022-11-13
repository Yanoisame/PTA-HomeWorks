def gys(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


num1, num2 = map(int, input().split())
k = gys(num1, num2)
print(k, num1 * num2 // k)
