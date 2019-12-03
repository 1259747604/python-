# 就是generator 可以next往下走 一般直接迭代使用
print((x*x for x in range(1,11)))
g = (x*x for x in range(1,11))
for i in g:
  print(i)

# 斐波拉契数列
def fib(max):
  n,a,b=0,0,1
  while n < max:
    print(b)
    # t = (b,a+b)
    # a = t[0]
    # b = t[1]
    # 注释步骤可写成
    a,b=b,a+b
    n += 1
fib(6)
# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fibg(max):
  n,a,b=0,0,1
  while n < max:
    yield b
    a,b=b,a+b
    n += 1
  return 'done'
print(fibg(6))

for k in fibg(6):
  print(k)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fibg(6)
while True:
  try:
    x = next(g)
    print('g:',x)
  except StopIteration as e:
    print(e.value)
    break

# 杨辉三角
def triangles():
  L=[1]
  while True:
    yield L
    L1 = [1]
    for i in range(1,len(L)):
      L1.append(L[i-1]+L[i])
    L1.append(1)
    L = L1
n= 0
result = []
for t in triangles():
  result.append(t)
  n += 1
  if n == 10:
    break

print(result)
