def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

# 携带参数
def log1(text):
  def decorator(func):
    def wrapper(*args, **kw):
        print('%s %s():' %(text,func.__name__))
        return func(*args, **kw)
    return wrapper
  return decorator

# 相当于 log1('22')(now1)
@log1('22')
def now1():
    print('2015-3-25')

now1()

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
# 处理方法
import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# 练习
# 运行时间
import time
def metric(fn):
  @functools.wraps(fn)
  def wrapper(*args,**kw):
    start = time.time()
    fn(*args,**kw)
    end = time.time()
    print('%s executed in %s ms' % (fn.__name__, end - start))
    return 
  return wrapper

@metric
def test1():
  print('测试运行时间')

test1()

# 简略版带参或者不带参
def log2(txt):
  if isinstance(txt,str):
    def metric(fn):
      @functools.wraps(fn)
      def wrapper(*args,**kw):
        start = time.time()
        fn(*args,**kw)
        end = time.time()
        print('%s %s in %s ms' % (fn.__name__,txt, end - start))
        return 
      return wrapper
    return metric
  else:
    @functools.wraps(txt)
    def wrapper(*args,**kw):
      start = time.time()
      txt(*args,**kw)
      end = time.time()
      print('%s executed in %s ms' % (txt.__name__, end - start))
      return 
    return wrapper

@log2
def test2():
  print('aaa')

test2()

@log2('bbb')
def test2():
  print('bbb')

test2()
