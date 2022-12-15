'''
open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)
    文件对象的方法:
        f.read()/f.read(size)
        f.readline()/f.readlines()
        f.write()
        f.tell()
        f.seek()
        f.close()


pickle 模块:实现了基本的数据序列和反序列化
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
'''