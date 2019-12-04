# 查询素数

# 基数生成器
def _odd_iter():
  n = 1
  while True:
    n += 2
    yield n

# 筛选函数
def _not_divisible(n):
  return lambda x: x%n > 0

# 素数生成器
def primes():
  yield 2
  it = _odd_iter()
  while True:
    n =  next(it)
    yield n
    it = filter(_not_divisible(n), it)

for n in primes():
    if n < 10:
        print(n)
    else:
        break

# 过滤出回文数

# 过滤器
def is_palindrome(n):
  return n == int(str(n)[::-1])

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

