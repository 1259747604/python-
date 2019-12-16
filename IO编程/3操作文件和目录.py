import os
print(os.name)## 操作系统类型
# 要获取详细的系统信息，可以调用uname()函数
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
""" print(os.uname()) """
# 环境变量
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))
# 有返回 没有返回默认值
print(os.environ.get('x', 'default'))

# 操作文件和目录
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
""" os.mkdir(os.path.join(os.path.abspath('.'),'testdir')) """
# 删除目录
""" os.rmdir(os.path.join(os.path.abspath('.'),'testdir')) """
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
""" print(os.path.split(os.path.join(os.path.abspath('.'),'testdir'))) """

""" os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便 """
# 对文件重命名:
""" os.rename('test.txt', 'test.py') """
# 删掉文件:
""" os.remove('test.txt') """

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
# 理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
def main():
  str = input('输入查询字符串：')
  path_name = input('输入查询路径（默认为工作路径）:')
  if path_name == '':
    path_name = '.'
  minus = len(path_name)

  def list_file(str,path):
    list_all =os.listdir(path)
    for name_f in list_all:
      path_c = os.path.join(path,name_f) 
      if os.path.isfile(path_c) and str in os.path.splitext(name_f)[0]:
        print(path_c[minus:])#把路径前缀去掉
      elif os.path.isdir(path_c):
        list_file(str,path_c)
  list_file(str,path_name)

main()