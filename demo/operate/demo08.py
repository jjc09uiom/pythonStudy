'''
>>> 5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数( 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系)
0
>>> 17 % 3 # 取余
2
>>> 2 ** 5 # 乘方
32


:=  	海象运算符，可在表达式内部为变量赋值
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

位运算符

逻辑运算符:and or not

成员运算符(字符串，列表或元组):in\not in

身份运算符(比较两个对象的存储单元):is\is not


在交互模式中，最后被输出的表达式结果被赋值给变量 _
ex:
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625


数学函数
随机数函数
三角函数
数学常量
'''
'''
list could do same operate like string,but could save different type of var and could be changed
list own many method to use,like append();pop();
cut list could use third parameter to set serial interval 
    if the third parameter is \-1\ means reverse read

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]

'''
#ex:rolling-over the string
def reverseWords(input):
     
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]
 
    # 重新组合字符串
    output = ' '.join(inputWords)
     
    return output
 
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)




'''
tuple is similar with list but could'd change its elements

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )

actually, string is a unique kind of tuple

other cases:\0or1 element\--->tup1 = ()    # 空元组
                                tup2 = (20,) # 一个元素，需要在元素后添加逗号
'''

'''
set 
创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

parame = {value01,value02,...}
或者
parame = set(value)

'''
#ex:
#!/usr/bin/python3
print("===========================")
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素


'''
dictionary:列表是有序的对象集合，字典是无序的对象集合
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的
'''
#ex:
#!/usr/bin/python3
print("=================================")
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (dict)
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

'''
dict()\clear()\keys()\values()
ex:
dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])-->{'Runoob': 1, 'Google': 2, 'Taobao': 3}
dict(Runoob=1, Google=2, Taobao=3)-->{'Runoob': 1, 'Google': 2, 'Taobao': 3}
{x: x**2 for x in (2, 4, 6)}-->{2: 4, 4: 16, 6: 36}

'''