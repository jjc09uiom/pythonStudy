'''
生成器:使用了 yield 的函数被称为生成器
在调用生成器运行的过程中
每次遇到 yield 时函数会暂停并保存当前所有的运行信息
返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行

ex:使用 yield 实现斐波那契数列
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield b
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
'''