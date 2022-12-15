'''
loop

1.while (condition):
        statements
or

whiel (expr):
    statements
else:
    additional_statements

python don't have do-while

use ctrl+c to get out from infinite loop

2.for (variable) in (sequence):
        statements
    else:
        statements

could through successive mountable iteration object


3.function---range()生成数列
ex:
>>>for i in range(5):
...     print(i)
...
0
1
2
3
4

or:指定区间的值
ex:
>>>for i in range(5,9) :
    print(i)
5
6
7
8


or:指定不同的增量,可以是负数
ex:
>>>for i in range(0, 10, 3) :
    print(i)
0
3
6
9


4.pass语句--pass 不做任何事情，一般用做占位语句
ex:
>>>while True:
...     pass  # 等待键盘中断 (Ctrl+C)

ex:最小的类
>>>class MyEmptyClass:
...     pass
'''

