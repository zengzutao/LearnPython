#----------------------------错误-----------------------
# 1.错误处理 try...except...finally...
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

# 2.调用堆栈
# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

# $ python3 err.py
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero

# 3.记录错误
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

#打印错误信息
# main()
# print('END')

# 4.抛出错误 raise语句抛出一个错误的实例
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

#--------------------------------调试--------------------------
# 1.print()把可能有问题的变量打印出
# 2.断言 assert

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# 启动Python解释器时可以用-O参数来关闭assert
# $ python3 -O err.py
# 关闭后，你可以把所有的assert语句当成pass来看

# 3.logging
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

import logging
logging.basicConfig(level=logging.INFO)

#4.pdb  -m pdb启动  l来查看代码 n可以单步执行代码 p 变量名来查看变量
# err.py
s = '0'
n = int(s)
print(10 / n)

# pdb.set_trace() p查看变量 c继续运行
# err.py 设置一个断点
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

#--------------------------------单元测试--------------------------
#  单元测试示例
#  1.编写单元测试 以test开头的方法就是测试方法
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): #不存在的key时，断言会抛出KeyError
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): #访问不存在的key时，我们期待抛出AttributeError
            value = d.empty

# 2.运行单元测试 
# 1).在文件上添加两行代码 
if __name__ == '__main__':
    unittest.main()
# 2).-m unittest直接运行单元测试
# $ python3 -m unittest mydict_test

# 3.setUp与tearDown
class TestDict(unittest.TestCase):
    
    def setUp(self):
        print('setUp...') #开启数据库连接

    def tearDown(self):
        print('tearDown...') #关闭数据库连接

# 3.文档测试 doctest 直接提取注释中的代码并执行测试

# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
