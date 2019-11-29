# 转义
print('hello\' \"world\"')
# r''默认不转义
print(r'aa+ss+ss""')
# 换行显示
print('''aa
bb
cc''')
print(r'''a
b
c''')
print(r'''hello,\n
world''')

# boolean
# 且
print(True and False)
# 或
print(True or False)
# 非
print(not True)
# if
age = 16
if age > 18:
  print('成年')
else:
  print('未成年')
# 动态类型 可改变类型
a = 1
print(a)#数字
a = '11'
print(a)#字符串

a = 'aa' #内存中创建a的变量 创建字符串'aa' 将a指向字符串
b = a #将 b指向a指向的字符串'aa'
a = 'bb'#创建字符串'bb' 将a指向它
print(b)#所以打印的结果是'aa'

#除法
print(10/3)
print(10//3)#向下取整
print(10%3)#取余数