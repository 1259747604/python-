# dict 讲道理不就是对象吗
a = {'a':1,'b':2,'c':3}
print(a['a'])

# 判断是否存在
print('d' in a)
print(a.get('d'))#没有返回none
print(a.get('d',4))#没有返回设定的值4

# 删除属性
a.pop('a')
print(a)

# set set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
b = set([1, 1, 2, 2, 3, 3])
print(b)
# 添加
b.add(4)
print(b)
# 删除
b.remove(4)
print(b)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
c = set([1,2,3,4,5])
d = set([2,3,5,6,7])
print( c & d)#交集
print( c | d)#并集

# 不可变对象
# replace方法创建了一个新字符串'Abc'并返回 并不是修改'abc' 所以'adc'是不可变的
e = 'abc'
print(e.replace('a','A'))
print(e)

# tuple是不可变对象 可放入dict中
f = {(1,2):'2'}
print(f[(1,2)])
# 如果元组里有可变对象list则不能作为dict的key
# g = {(1,[1,2]:'3')}
# print(g[(1,[1,2])])

# set同理
g = set([(1,2)])
print(g)


