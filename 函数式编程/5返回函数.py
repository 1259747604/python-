# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
  def sum():
    s = 0
    for n in args:
      s += n
    return s
  return sum

f = lazy_sum(1,2,3,5,6)
print(f)#返回的是函数
print(f())
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易

# 练习 计数器
def createCounter():
  n = 0
  def counter():
    nonlocal n
    n += 1
    return n
  return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())