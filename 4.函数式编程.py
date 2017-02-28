# 1.高阶函数(Higher-order function):
# 1).变量可以指向函数
# 2).函数名也是变量
# 3).传入函数

# 编写高阶函数，就是让函数的参数能够接收别的函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

# 2. map()（）/reduce() 接收一个函数和一个序列
# 1) map：list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])) 把list转换成字符串(str是python内置的函数)
# 2) reduce：
# 示例

from functools import reduce

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# 3.filter() 过滤 接收一个函数和一个序列
# filter()的作用是从一个序列中筛出符合条件的元素

def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

# 4.sorted() 排序

# 忽略字符串大小写的排序方法
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

# 反向排序 reverse=True
 sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

# 5.函数作为返回值

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 6.匿名函数

lambda x: x * x

# 7.装饰器(decorator) 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

import functools

#无参
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#有参
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
    print('2015-3-25')
# 备注：@log 相当于 now = log(now)

# 8.偏函数（Partial function）把一个函数的某些参数给固定住（也就是设置默认值）

int2 = functools.partial(int, base=2)

