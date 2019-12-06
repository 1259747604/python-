class One(object):
  def one(self):
    print('one')


class Two(object):
  def two(self):
    print('two')

class Child(One,Two):
  pass

c = Child()
c.one()
c.two()