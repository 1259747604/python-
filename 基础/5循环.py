a = ['a','b','c']
for i in a:
  print(i)

# range()函数 可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
sum = 0
for i in range(101):
  sum += i
print(sum)

# while
sum = 0
n = 99
while n > 50:
  sum += n
  n -= 2
print(sum)

# break
n = 1
i = 0
while n < 100:
  i += n
  if i > 10:
    print(i)
    break
  n += 1
print(i)

# continue
n = 0
while n < 10:
  n+=1
  if n%2 == 0:
    continue
  print(n)

