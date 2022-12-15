'''
列表:列表可以修改，而字符串和元组不能
    basic function:.append(x)/.remove(x)&&.clear()/.insert(i,x)


将列表当做堆栈使用:
用 append() 方法可以把一个元素添加到堆栈顶
用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来

将列表当作队列使用:
在列表的最后添加或者弹出元素速度快
然而在列表里插入或者从头部弹出速度却不快
（因为所有其他的元素都得一个一个地移动）
ex:
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'


列表推导式:提供了从序列创建列表的简单途径

嵌套列表解析:
ex:将3X4的矩阵列表转换为4X3列表
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


del 语句:从一个列表中根据索引来删除一个元素，而不是值来删除元素
可以用 del 语句从列表中删除一个切割，或清空整个列表

遍历技巧:
在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
同时遍历两个或更多的序列，可以使用 zip() 组合
    for q, a in zip(questions, answers):

要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值

'''