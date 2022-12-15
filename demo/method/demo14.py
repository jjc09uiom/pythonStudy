'''
迭代器:是访问集合元素的一种方式,迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退

基本的方法：iter() 和 next()

字符串，列表或元组对象都可用于创建迭代器
ex:
>>> list=[1,2,3,4]
>>> it = iter(list)    # 创建迭代器对象
>>> print (next(it))   # 输出迭代器的下一个元素
1
>>> print (next(it))
2

ex:
list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=" ")

ex:
import sys

list = [1,2,3,4]
it  = iter(list)

while True :
    try:
        print(next(it))
    except StopIteration:
        sys.exit()



创建一个迭代器:把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
ex:创建一个返回数字的迭代器，初始值为 1，逐步递增 1
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


>>1 2 3 4 5




StopIteration异常:用于标识迭代的完成，防止出现无限循环的情况
ex:在 20 次迭代后停止执行
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)
'''