year, month, day = map(int, input().split("/"))
days = 0
dic = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    dic['2'] = 29
if int(month) > 1:
    for obj in dic.keys():
        if month == int(obj):
            for i in range(1, int(obj)):
                days += dic[str(i)]
    days += day
else:
    days = day
print(days)
