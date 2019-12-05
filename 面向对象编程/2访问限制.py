# 练习
# 把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
      return self.__gender
    def set_gender(self,gender):
      if isinstance(gender,str):
        self.__gender = gender
      else:
        self.__gender = 'error'

a = Student('tt','tt')
print(a.get_gender())
a.set_gender('male')
print(a.get_gender())
a.set_gender(1)
print(a.get_gender())