#!/usr/bin/python3

#Fibonacci series
#两个元素的总和确定了下一个数
a,b = 0,1
while b < 100 :
    print(b,end=" ")
    a,b = b,a+b
