list1 = list(range(100))

# 0,1,2
print(list1[0:3])
print(list1[:3])

# 从后找
print(list1[-1])
print(list1[-5:-1])

# 前10个数每两个取一个
print(list1[:10:2])

# 每10个取一个
print(list1[::10])

# 复制
list1[:]

# 字符串和元组也可以用切片