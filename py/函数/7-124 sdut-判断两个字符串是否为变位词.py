t1 = str(input()).replace(".", "")
t2 = str(input()).replace(".", "")
temp1 = 0
temp2 = 0
for i in t1:
    for k in t2:
        if i == k:
            temp1 += 1
        else:
            temp2 += 1
if len(t1) == temp1 or len(t2) == temp2:
    print("yes")
else:
    print("no")