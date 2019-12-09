# 很多时候，数据读写不一定是文件，也可以在内存中读写。

# StringIO顾名思义就是在内存中读写str。
from io import StringIO
f = StringIO('aaa')
# 用于获取初始化的内容
print(f.read())
f.write('bbb')
# 用于获取写入后的内容
print(f.getvalue())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
# 差不多