# list 就是个数组
classmates = ['Michael', 'Bob', 'Tracy']

print(classmates[0])
print(len(classmates))
print(classmates[-1])
classmates.append('tt')
print(classmates)
classmates.insert(1,'tt')
print(classmates)
print(classmates.pop(0),classmates)

# tuple 元组 tuple和list非常类似，但是tuple一旦初始化就不能修改
t = ('a','b','c')
print(t[0])
# 定义一个空tuple
empty = ()
print(empty)
# 定义只有一个元素的tuple
only = (1,)
print(only)