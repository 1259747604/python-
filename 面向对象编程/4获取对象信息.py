# 使用type()
print(type('aa'))
print(type(123))
print(type(None))
print(type(abs))
# 判断类型是否相同
print(type('aa') == str)
print(type('aa') == int)
# 判断是否是函数
import types
def fn():
  pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda  x: x*x) == types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1,2,3],(tuple,list)))

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir(str))
print('aa'.__len__(),len('aa'))


class Test(object):
  def __init__(self):
    self.name = 'test'
    self.__nname = 'test'
  
a = Test()
# getattr
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(a,'name'))
print(getattr(a,'bname',404))
# setattr
print(setattr(a,'name','aa'))
# hasattr
print(hasattr(a,'name'))
print(hasattr(a,'__nname'))