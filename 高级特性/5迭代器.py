# 凡是可作用于for循环的对象都是Iterable类型；
  # 一类是集合数据类型，如list、tuple、dict、set、str等
  # 一类是generator，包括生成器和带yield的generator function

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
from collections.abc import Iterator
print(isinstance(iter([]), Iterator))
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass