# 定义函数用def
def f(a):
  if(a > 6):
    return '666'
  else:
    return '6'

print(f(7))

# 定义一个空函数
# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def no():
  pass
# pass还可以用在其他语句里，比如
#缺少了pass，代码运行就会有语法错误
# if age >= 18:
#     pass

# 参数类型检查
# def check(a):
#   if not isinstance(a,(int,float)):
#     raise TypeError('bad operand type')
#   if a >= 0:
#     return a
#   else:
#     return -a

# print(check('A'))#弹出报错

# 返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

r = move(100, 100, 60, math.pi / 6)
print(r)#其实返回多个值返回的是一个元组

# 练习
def quadratic(a, b, c):
  top1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
  top2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
  return top1,top2
a,b = quadratic(2, 3, 1)
print(a,b)
