class Student(object):
  def __init__(self):
    pass
print(Student())#打印的有点丑

class Student1(object):
  def __init__(self):
    pass
  def __str__(self):
    return '好看的'
  __repr__ = __str__
print(Student1())

s = Student1()
s

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
  def __init__(self):
    self.a = 0
    self.b = 1
  def __iter__(self):
    return self
  def __next__(self):
      self.a, self.b = self.b, self.a + self.b
      if self.a > 20:
        raise StopIteration()
      return self.a

f = Fib()
for n in f:
  print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
def __getitem__(self, n):
  a, b = 1, 1
  for x in range(n):
    a, b = b, a + b
  return a
Fib.__getitem__ = __getitem__
print(f[2])

# 但是list有个神奇的切片方法
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
def getitem1(self, n):
    if isinstance(n, int): # n是索引
      a, b = 1, 1
      for x in range(n):
        a, b = b, a + b
      return a
    if isinstance(n, slice):
      start = n.start
      stop = n.stop
      if start == None:
        start = 0
      a, b = 1, 1
      L = []
      for x in range(stop):
        if x >= start:
          L.append(a)
        a, b = b, a + b
      return L

Fib.__getitem__ =getitem1
print(f[2])
print(f[:5])
print(f[2:5])

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下
# 返回函数也是完全可以的
class Student1(object):

  def __init__(self):
      self.name = 'Michael'

  def __getattr__(self, attr):
      if attr=='score':
          return 99
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)


# __call__
# 一个对象实例可以有自己的属性和方法，
# 当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的
# __call__()还可以定义参数

class Test(object):
  def __init__(self,name):
    self.name = name
  def __call__(self):
    print(self.name)
  
t = Test('aa')
t()

# 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例

print(callable(Student()))
print(callable(Student1()))
print(callable(Test('aa')))
print(callable([]))

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
