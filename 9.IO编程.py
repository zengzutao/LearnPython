# 同步和异步的区别就在于是否等待IO执行的结果
# 异步编程模型：回调模式 轮询模式

1.文件读写

1).读文件
(1).open() 打开文件
(2).read() 读文件 
(3).close()关闭
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#自动调用close方法
with open('/path/to/file', 'r') as f:
    print(f.read())

# 文件大小 read(size)获取读取文件的大小 readline()每次读取一行

二进制文件 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
open('/Users/michael/test.jpg', 'rb')

file-like Object 常用作临时缓冲

字符编码 需要给open()函数传入encoding参数
open('/Users/michael/gbk.txt', 'r', encoding='gbk')


2).写文件 传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

open()函数传入encoding参数，将字符串自动转换成指定编码


2.StringIO和BytesIO

1).StringIO StringIO操作的只能是str
from io import StringIO
f = StringIO()
f.write('hello')
f.getvalue() 方法用于获得写入后的str

2).BytesIO 操作二进制数据
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

3.操作文件和目录(os)

1).环境变量 os.environ

2).操作文件和目录
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 合成路径：os.path.join() 
# 拆分路径：os.path.split() 
# 直接获取文件扩展名：os.path.splitext()
>>> os.path.join('/Users/michael', 'testdir') 

'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')

列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]

列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


3.序列化

