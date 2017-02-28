# 1.切片(slice) (L代表List) 简化循环取值
# 取前三个：L[0:3]
# 复制：L[:]
# 取后10个：L[-10]
# 取L后两个：L[-2:]
# 取倒数第二个：L[-2:-1]

# 2.迭代：for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration) Iterable

# Python 迭代是通过 for ... in 实现的,for也可以，但是要判断是否为可迭代对象
# 1).如何判断一个对象是可迭代对象呢？ 
# from collections import Iterable
# isinstance('abc', Iterable) 

# 下标循环： Python内置的enumerate函数可以把一个list变成索引-元素对
# for i, value in enumerate(['A', 'B', 'C'])

#同时引用两个变量
# for x, y in [(1, 1), (2, 4), (3, 9)]:
# print(x, y)

# 3.列表生成式

# 1) list(range(1, 11)) 生成为 list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2) [x * x for x in range(1, 11)] 生成为 [1x1, 2x2, 3x3, ..., 10x10]
# 3) [m + n for m in 'ABC' for n in 'XYZ'] 生成为 ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 4.生成器 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 1) list L = [x * x for x in range(10)]
# 2) generator g = (x * x for x in range(10)) for n in g
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 5.迭代器 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值(Iterator)

# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的
