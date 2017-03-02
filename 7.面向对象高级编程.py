# 1 __slots__ 限制实例的属性

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 2 @property  负责把一个方法变成属性

class Student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 3.多重继承 一个子类就可以同时获得多个父类的所有功能 MixIn 混入模式

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

#我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类

# 4.定制类 
# (1).__str__() 返回字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

# (2).__iter__() 返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

# (3).__getitem__() 按照下标取出元素  
# __setitem__() 把对象视作list或dict来对集合赋值
# __delitem__() 删除元素

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# f[:10:2] f[2]

# (4).__getattr__() 动态返回一个属性 默认返回就是None
class Student(object):
    
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
    # 抛出AttributeError的错误 只返回特定属性
    def __getattr__(self, attr): 
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

#动态获取API名称 链式调用
class Chain(object):
    
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# (5).__call__() 对实例进行调用
# callable()函数，我们就可以判断一个对象是否是“可调用”对象
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


# 5.使用枚举类
# 1). 自定义枚举类

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 2).精确地控制枚举类型,可以从Enum派生出自定义类

@unique #@unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 6.使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

# 1).type() 既可以返回一个对象的类型，又可以创建出新的类型

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

# 动态创建类，需要传入的参数
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上

# 2).metaclass(创建类或者修改类) 编写一个ORM框架
# 控制类的创建行为 先定义metaclass，就可以创建类，最后创建实例  
# 默认习惯，metaclass的类名总是以Metaclass结尾
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass




