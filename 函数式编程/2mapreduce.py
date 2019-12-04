def f(x):
  return x*x
r = map(f,list(range(1,11)))
print(r)
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 数列求和
# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce
from functools import reduce
def add(a,b):
  return a+b

t = reduce(add,list(range(1,11)))
print(t)

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def ch(a,b):
  return a*10 + b
t = reduce(ch,[1,3,5,7,9])
print(t)

# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，
# 对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
def char2num(s):
  digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
  return digits[s]

c = reduce(ch,map(char2num,'13579'))
print(c)

# 练习
# 首字母大写其余小写
def normalize(name):
  return str.upper(name[0])+str.lower(name[1:])


print(list(map(normalize,['adam', 'LISA', 'barT'])))

# 接受一个list求积
def prod(L):
  return reduce(lambda a,b: a*b,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 浮点字符串转换为浮点数
def str2float(s):
  n = s.index('.')
  digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

  def char2num(s):
    return digits[s]

  str1 = s[0:n]
  str2 = s[n+1:]

  o = reduce(lambda a,b: a*10+b,map(char2num,str1))
  t = reduce(lambda a,b: a*10+b,map(char2num,str2))/(10**len(str2))
  return o + t

print(str2float('123.456'))
# print(float('123.456'))