#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'TT'
# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
import sys

def hello():
  if len(sys.argv) == 1:
    print('hello world')
  elif len(sys.argv) == 2:
    print('hello world %s' %sys.argv[1])
  else:
    print('wow')

# Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，
# if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == "__main__":
  hello()


