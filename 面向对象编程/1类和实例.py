# 有点简单 
class Student(object):
  def __init__(self,name,score):
    self.name = name
    self.score =score
  def _print(self):
    print('%s考了%s' %(self.name,self.score))
  def _getGrade(self):
    if self.score > 80:
      print('A')
    elif self.score <=80 and self.score > 60:
      print('B')
    else:
      print('C')

a = Student('aa',88)
a._print()
a._getGrade()
b = Student('bb',66)
b._getGrade()
b._print()