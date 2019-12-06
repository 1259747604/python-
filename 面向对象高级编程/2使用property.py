class Screen(object):
    @property
    def width(self):
      return self._width

    @width.setter
    def width(self,width):
      if not isinstance(width,int):
        raise ValueError('width must be an integer!')
      if width < 0 or width > 100:
        raise ValueError('不合适')
      self._width = width
    
    @property
    def height(self):
      return self.height

s = Screen()
# s.width = -1 会报错
s.width = 20
print(s.width)