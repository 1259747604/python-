# 内容读取到内存
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
""" try:
    f = open('C:/Users/Administrator/Desktop/work/徐汇/拘留所可视化/拘留所修改意见.docx','r')
    print(f.read())
finally:
    if f:
        f.close() """

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用
with open('C:/Users/Administrator/Desktop/1.txt','r') as f:
  # print(f.read(10))
  # print(f.readlines())
  for i in f.readlines():
    print(i)

# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('C:/Users/Administrator/Desktop/3.png','rb') as f1:
  print(f1.read(10))

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
# with open('C:/Users/Administrator/Desktop/1.txt','r',encoding='gbk', errors='ignore') as f:

# 写文件
with open('C:/Users/Administrator/Desktop/1.txt','a') as f2:
  # f2.write('aaa')
  #如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
  f2.write('aaabbb')
