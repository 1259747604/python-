# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义
# 好处是简单，缺点是类型是int，并且仍然是变量
# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能
from enum import Enum,unique
Month  = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
print(Month.__members__.items())
for name, member in Month.__members__.items():
  print(name, '=>', member, ',', member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Week(Enum):
  Sun = 0 # Sun的value被设定为0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6

day = Week.Sun
print(day.value)

# 可看地址 https://segmentfault.com/a/1190000017327003

#练习 
class Gender(Enum):
  Male = 0
  Female = 1

class Student(object):
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')