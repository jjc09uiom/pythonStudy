'''
1.输出格式美化
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。


.rjust():返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
类似的方法, 如 ljust() 和 center()
zfill(), 它会在数字的左边填充 0

str.format() 的基本使用如下:
    >>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
    菜鸟教程网址： "www.runoob.com!"

    >>> print('{0} 和 {1}'.format('Google', 'Runoob'))
    Google 和 Runoob
    >>> print('{1} 和 {0}'.format('Google', 'Runoob'))
    Runoob 和 Google

保留到小数点后三位:
>>> import math
>>> print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
常量 PI 的值近似为 3.142。

% 操作符也可以实现字符串格式化
>>> import math
>>> print('常量 PI 的值近似为：%5.3f。' % math.pi)
常量 PI 的值近似为：3.142。




'''