#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' # 文档注释

__author__ = 'Michael Liao' # 作者

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':  #运行测试
    test()

# 作用域 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

# 第三方模块 PIL 图像处理库