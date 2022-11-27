# #################字典的创建(必须是不可变类型)#################
# 1. {}
# 2. dict(可迭代对象)，每个可迭代对象必须有两个分量(第一个分量作为关键字，第二个分量作为值)
# 3. dict(字典类型).fromkeys(一组关键字,值(默认为空，可以自定义，所有key采用这个值))
# 4. dict.from(seq, value = None),以seq为关键字，以Value为默认值创建字典
# 5. dict(zip(可迭代对象1, 可迭代对象2))  拉链方法组成字典,以小的开始结合


# #################字典推导式(字典格式简写)#################
# {关键字表达式: 元素值表达式 for 循环变量 in 对象 [if 条件表达式]}


# #################字典元素访问与修改(增加，删除)#################
# 1. 访问操作
# 索引关键字，字典对象[关键字],对于访问操作，若没有该关键字将会报错

# 2. 访问操作(词频统计常用)
# 赋值对象 = 字典对象.get(关键字, 返回值) 若字典关键字存在，将返回对应的元素值;关键字不存在将返回指定值（不写为空）

# 3. 写操作
# 字典对象[关键字]，若不存在，将会新增
# 字典对象.update(含有两个分量的可迭代对象) 批量更新字典元素值，没有的将新增，如果为空将什么不做

# 4.字典的删除
#  字典对象.pop(key, 不存在关键字时的返回值) 可以移除指定键值对，未指定返回值且关键字不存在时，会报错
#  字典对象.popitem() 删除最后一个键值对,空字典会报错
#  del 字典对象[关键字] 删除键值对,关键字不存在会报错,没有返回值
#  字典对象.clear() 清除字典键值对，剩下外壳


# #################字典的遍历循环#################
# 1. 按关键字遍历
# for 循环变量 in 字典对象(特殊)
# 常规语法：for 循环变量 in 字典.keys():  类似于集合产物
# 遍历字典关键字时,对值进行修改,循环内部加入：字典[循环变量] += 1

# 2.按键值对遍历
# 遍历出键值对(二元组)方法：for 循环变量 in 字典.items()
# 可以直接解包操作，for 循环变量1,循环变量2 in 字典.items()

# 3.按字典元素值遍历
# for 循环变量 in 字典.values()


# #################字典的其他操作#################
# 1. 常用函数
# 字典的排序: sorted,reversed
# 1.1字典排序常规用法
# sorted(字典对象.items(), key=lambda x: 条件函数)

# 可以使用内置函数,sum函数必须全部为数值类型,返回字典的key

# 2. 支持运算
