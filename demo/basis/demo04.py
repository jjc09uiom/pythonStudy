'''
1.int-ex:1
2.bool-ex:True
3.float-ex:1.23\3E-2
4.complex-ex:1+2j\1.1+2.2j
'''

'''
in python-------\'\ = \"\

use \'''\---->get Multi-line string

shift character---->\
    use \r\ make shift character ignored
    ex:r"this is a line with \n"----->print:this is a line with \n

cascade connection
    ex:"this " "is " "string"-------->this is string

use \+\ to connect strings
use \*\ to repeat strings

index:
1.from left yo right-start from 0
2.form right to left-start from -1

in python-char=string(strlen=1)

cut string by var[head_index:tail_index:lenth]

'''
#!/usr/bin/python3
 
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

'''
Python转义字符
Python字符串运算符
Python 字符串格式化----\%\

    字面量格式化字符串-->f-string
    ex:
    >>> name = 'Runoob'
    >>> f'Hello {name}'  # 替换变量
    'Hello Runoob'


    Unicode 字符串:在Python3中，所有的字符串都是Unicode字符串

    字符串内建函数
'''