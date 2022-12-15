'''
推导式:可以从一个数据序列构建另一个新的数据序列的结构体

列表推导式-->[表达式 for 变量 in 列表] or [表达式 for 变量 in 列表 if 条件]
ex:过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母
>>> names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
>>> new_names = [name.upper()for name in names if len(name)>3]
>>> print(new_names)
['ALICE', 'JERRY', 'WENDY', 'SMITH']

ex:计算 30 以内可以被 3 整除的整数
>>> multiples = [i for i in range(30) if i % 3 == 0]
>>> print(multiples)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

字典推导式:{ key_expr: value_expr for value in collection \if conditional\}
ex:使用字符串及其长度创建字典
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
>>> newdict = {key:len(key) for key in listdemo}
>>> newdict
{'Google': 6, 'Runoob': 6, 'Taobao': 6}

集合推导式:{ expression for item in Sequence \if conditional\}
ex:判断不是 abc 的字母并输出
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
>>> type(a)
<class 'set'>

元组推导式（生成器表达式）:(expression for item in Sequence \if conditional\)
ex:生成一个包含数字 1~9 的元组
>>> a = (x for x in range(1,10))
>>> a
<generator object <genexpr> at 0x7faf6ee20a50>  # 返回的是生成器对象

>>> tuple(a)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
(1, 2, 3, 4, 5, 6, 7, 8, 9)
'''
