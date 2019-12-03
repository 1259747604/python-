# 生成[1-10]
print(list(range(1,11)))
# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x*x for x in range(1,11)])
# 筛选出偶数的平方
print([x*x for x in range(1,11)if x%2 == 0])
# 使用两层循环，可以生成全排列
print([x+y for x in 'ABC' for y in 'XYZ'])

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
print([d for d in os.listdir('.')])

# 使用两个变量生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k,v in d.items()])

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 练习
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)])