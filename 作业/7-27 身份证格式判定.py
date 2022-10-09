a = input()
ws = a[:17]
ls = a[-1:]
if len(a) == 18 and str.isdigit(ws) == True and ls.isalnum()== True:
    print("True")
else:print("False")