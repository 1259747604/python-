class Student(object):
  pass

s = Student()

s.name = 'aa'

# 绑定方法
def set_score(self,score):
  self.score = score

from types import MethodType

s.set_score = MethodType(set_score,s)

s.set_score(99)
print(s.score)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# 为了给所有实例都绑定方法，可以给class绑定方法：

Student.set_score = set_score

s1 = Student()
s1.set_score(88)
print(s1.score)

# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
class Student1(object):
  __slots__ = ('name','age')

s2 = Student1()
s2.name = 'aa'
s2.age = 18
s2.score = 20#会报错


