A = eval(input())
if type(A) is not int:
    print("值错误，您必须输入数值")
elif A == 0:
    print("算术错误，您不能输入0")
else:
    print(f"""20除以3的结果是: {20/int(A):.2f}
没有出现异常""")
