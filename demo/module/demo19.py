'''
1.import:引入某一模块

ex:
#!/usr/bin/python3
# 文件名: using_sys.py
 
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')



=============================
$ python using_sys.py 参数1 参数2
命令行参数如下:
using_sys.py
参数1
参数2

Python 路径为： xxx





2.from...import...:从模块中导入一个指定的部分
ex:
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377


3.from...import*:>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377

4.__name__属性:如果我们想在模块被引入时，
            模块中的某一程序块不执行，
            我们可以用__name__属性来使该程序块仅在该模块自身运行时执行

        ex:
        #!/usr/bin/python3
        # Filename: using_name.py

        if __name__ == '__main__':
            print('程序自身在运行')
        else:
            print('我来自另一模块')

    * 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入



5.dir() 函数:找到模块内定义的所有名称,以一个字符串列表的形式返回

ex:
>>> import fibo
>>> dir(fibo)
['__name__', 'fib', 'fib2']


6.标准模块
7.包
'''