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

#总结：
# 1.定义函数时，需要确定函数名和参数个数；

# 2.如果有必要，可以先对参数的数据类型做检查；

# 3.函数体内部可以用return随时返回函数结果；

# 4.函数执行完毕也没有return语句时，自动return None。

# 5.函数可以同时返回多个值，但其实就是一个tuple。
