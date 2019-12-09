import pickle
d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
""" pickle.dumps(d) """
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
with open('./testdir/dump.txt', 'wb') as f:
  pickle.dump(d,f)
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
with open('./testdir/dump.txt', 'rb') as f1:
  d = pickle.load(f1)
  print(d)

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系


# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
# 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
# 也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
import json
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
print(json.dumps(d))
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
class Student(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score

s = Student('Bob', 20, 88)
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(std):
  return {
    'name': std.name,
    'age': std.age,
    'score': std.score
  }
print(json.dumps(s,default=student2dict))
# 我们可以偷个懒，把任意class的实例变为dict
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(s,default=lambda x: x.__dict__))

# 反序列化为对象
def dict2student(d):
  return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))

obj = dict(name='小明', age=20)
# ensure_ascii默认情况是True，这时会把中文转成Unicode码，设置成False的话就是打印中文
s = json.dumps(obj, ensure_ascii=True)
print(s)