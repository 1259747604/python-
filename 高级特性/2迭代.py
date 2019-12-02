# 不就是for in吗
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
  print(key)

# 键值
for k,v in d.items():
  print(k,v)

# 迭代值
for v in d.values():
  print(v)

# 迭代字符串
for c in 'abc':
  print(c)

# list迭代索引
for i,v in enumerate([1,2,3]):
  print(i,v)

# 同时引用两个变量
for x,y in [(1,2),(3,4),(5,6)]:
  print(x,y)

def findMinAndMax(L):
  if L == []:
    return (None,None)
  min = 0
  max = 0
  for i in L:
    if(i<min):
      min = i
    if(i>max):
      max = i
  return (min,max)
print(findMinAndMax([]))
print(findMinAndMax([7]))