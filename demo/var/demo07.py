'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
'''
#!/usr/bin/python3

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

#多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"

'''
标准数据类型
1.Number（数字）
2.String（字符串）
3.List（列表）
4.Tuple（元组）
5.Set（集合）
6.Dictionary（字典）
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）


查询变量所指的对象类型
type()
ex:
>>> a, b, c, d = 20, 5.5, True, 4+3j
>>> print(type(a), type(b), type(c), type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>


isinstance()
ex:
>>> a = 111
>>> isinstance(a, int)
True

区别:
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。





删除对象引用 del
ex:
del var--删除单个对象
del var_a, var_b--删除多个对象
'''


