print( sorted([36, 5, -12, 9, -21]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21],key=abs))
# 字符串忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 反序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))

# 练习
L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return str(t[0]).lower()

def by_score(t):
    return t[1]

print(sorted(L,key=by_name))
print(sorted(L,key=by_score))