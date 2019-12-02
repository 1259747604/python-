# 参数顺序 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 可变参数
num = [1,2,3]

def f1(*n):
  sum = 0
  for i in n:
    sum += i  
  print(sum)
f1(*num)

#命名关键字参数 在*号后的参数
def f2(a,b,*,c):
  print('a:',a,'b',b,'c',c)

f2(1,2,c=3)
f2(1,2,**{'c':4})

# 关键字参数
def f3(a,b,**kw):
  print(kw)
f3(1,2,c=1,d=1)

t = {'c':1,'d':1}
f3(1,2,**t)

# 多个数乘积
def product(*arg):
  sum = 1
  for i in arg:
    sum *= i
  return sum

print(product(5))
print(product(5,6))
print(product(5,6,7))
print(product(5,6,7,9))