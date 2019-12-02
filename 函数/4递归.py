# 会栈溢出
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
# 栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
# def fact(n):
#   if n == 1:
#     return 1
#   return n*fact(n-1)


# print(fact(100))

# 尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
  return fact_iter(n,1)

def fact_iter(n,p):
  if n == 1:
    return p
  return fact_iter(n-1,n*p)
# print(fact(1000))
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。?????那有毛线用

# 汉诺塔
def move(n,a,b,c):
  if n == 1:
    print(a,'--->',c)
  else:
    move(n-1,a,c,b)
    print(a,'--->',c)
    move(n-1,b,a,c)

move(5,'A','B','C')
