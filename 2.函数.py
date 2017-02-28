import math

# 函数定义 defunName(参数)： 

# 参数检查

# 空函数
def nop():
    pass

# 多个返回值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 总结：
# 1.定义函数时，需要确定函数名和参数个数；

# 2.如果有必要，可以先对参数的数据类型做检查；

# 3.函数体内部可以用return随时返回函数结果；

# 4.函数执行完毕也没有return语句时，自动return None。

# 5.函数可以同时返回多个值，但其实就是一个tuple。

# 函数参数

# 1.设置默认参数（n=2） 指向不变的对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#  2.可变参数
#  1).定义一个list或tuple参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# calc([1, 2, 3]) list
# 14
# calc((1, 3, 5, 7)) tuple
# 84

# 2).参数前面加了一个 * 号(简写)
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# calc(1, 2)
# 5
# calc()
# 0

# 3.关键字参数 关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# person('Michael', 30)
# name: Michael age: 30 other: {}

# 4.命名关键字参数 

# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
# person('Jack', 24, city='Beijing', job='Engineer')
# Jack 24 Beijing Engineer

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去


#函数参数 总结：
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


# 递归函数 尾递归：在函数返回的时候，调用自身本身，尾递归优化，可以有效防止栈溢出

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。