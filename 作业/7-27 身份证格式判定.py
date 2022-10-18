a = input()
ws = a[:17]
ls = a[-1:]
if len(a) == 18 and ws.isdigit() == True and ls.isnumeric() == True:
    print("True")
else:
    print("False")
