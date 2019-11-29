print(ord('A'))#单个字符串转化为Unicode
print(ord('中'))#单个字符串转化为Unicode
print(chr(66))#转换为对应字符
print(chr(25991))#转换为对应字符

# str变为bytes为单位 转码与解码
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
x = b'ABC'
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes中包含无法解码的字节，decode()方法会报错
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# str包含多少字符
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，
# 在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，
# 为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 字符串格式化
#%2d位数
#%02d补0
print('Hello,%s' %'TT')
print('Hello,%d %s' %(2020,'year'))
print('%2d-%02d' % (3, 1)) # 3-01
print('%.2f' % 3.1415926)#3.14
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，
# 不过这种方式写起来比%要麻烦得多：
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = ((s2-s1)/s1)*100
print('提高了%.1f%%'%r)#第一种
print('提高了{0:.1f}%'.format(r))#第二种