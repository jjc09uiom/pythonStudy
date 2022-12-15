'''
异常处理
try/except
异常捕捉可以使用 try/except 语句

try:
        normal statements
except:
        statements while the exceptions happened


try 语句按照如下方式工作；
1.执行 try 子句
2.如果没有异常发生，忽略 except 子句，try 子句执行后结束。
3.如果发生了异常，那么 try 子句余下的部分将被忽略
4.如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
5.如果异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常
    最多只有一个分支会被执行。

处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
    except (RuntimeError, TypeError, NameError):


最后一个except子句可以忽略异常的名称，它将被当作通配符使用
你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
    except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


try/except...else
else 子句将在 try 子句没有发生任何异常的时候执行


try-finally 语句
无论是否发生异常都将执行最后的代码


raise:抛出异常


用户自定义异常:创建一个新的异常类来拥有自己的异常
异常类继承自 Exception 类，可以直接继承，或者间接继承
    ex:
        >>> class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


定义清理行为
try 语句还有另外一个可选的子句
它定义了无论在任何情况下都会执行的清理行为


'''