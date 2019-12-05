# 讲道理没啥意思


class Animal(object):
  def run(self):
    print('哈哈哈')

class Dog(Animal):
  def run(self):
    print('dog在哈哈哈')

def run_twice(a):
  a.run()
  a.run()

run_twice(Dog())