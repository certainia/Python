# 集合（set）的详细操作

# 1. 定义和创建集合
# 集合与数学中的集合概念一致，用于存储不重复的元素，且内部无序
# 注意：直接使用 {……} 定义非空集合；若 {} 内部为空，会被识别为空字典，
#       定义空集合时必须使用 set() 函数
s1 = {1, 2, 3, 4}     # 定义非空集合
# s_empty = {}        # 错误！这会被识别为空字典
s_empty = set()       # 正确的空集合定义
# 除了set外 都可以使用list()/[]定义空集  [] () '' {}

# 通过 set() 将其他可迭代对象转换为集合（自动去重）
lst = [1, 2, 2, 3, 4, 4, 5]
s_from_list = set(lst)
print("从列表转换的集合:", s_from_list)  # 输出: {1, 2, 3, 4, 5}


# 2. 集合的常用方法
# 2.1 添加元素：add() 与 update()
s = {1, 2, 42, 5}
s.add(3)  # 添加单个元素3
print("添加元素3后:", s)

# update() 方法可将一个可迭代对象中的多个元素添加到集合中
t = [12, 3, 1, 2]
s.update(t)
print("使用 update() 后的集合:", s)


# 2.2 删除元素
# remove(x): 删除集合中的元素 x，若 x 不存在则会引发 KeyError
# discard(x): 删除元素 x，若 x 不存在则不会报错
# pop(): 随机移除集合中的一个元素，并返回该元素，若集合为空则引发 KeyError
# clear(): 清空集合中所有元素

print("当前集合 s:", s)
# s.remove(21)    # 若21不存在，则会报错
s.discard(21)      # 若21不存在，不报错
removed_item = s.pop()  # 随机移除一个元素
print("pop() 移除的元素:", removed_item)
print("pop() 后的集合:", s)
s.clear()
print("clear() 后的集合:", s)

# 2.3 判断关系与集合间的运算
# isdisjoint(): 判断两个集合是否没有交集
# issubset(): 判断当前集合是否为另一个集合的子集
# issuperset(): 判断当前集合是否为另一个集合的超集
a = {1, 2, 3}
b = {4, 5}
c = {2, 3}

print("a 与 b 是否没有交集?", a.isdisjoint(b))  # True
print("c 是否为 a 的子集?", c.issubset(a))        # True
print("a 是否为 c 的超集?", a.issuperset(c))        # True


# 判断 s 是否为 t 的超集
print("s 是否为 t 的超集:", s.issuperset(t))
# issuperset() 可接受任意可迭代对象作为参数
# issuperset() 和 issubset() 都只能由集合（set）调用，且它们分别等价于 >=（超集） 和 <=（子集）
# issuperset() 的适用范围总结<同理适用于issubset>
# 可迭代对象类型	是否支持 issuperset()	是否需要转换
# 集合（set）	        ✅ 直接支持	        ❌
# 列表（list）	        ✅ 直接支持         	❌
# 元组（tuple）	        ✅ 直接支持	        ❌
# 字符串（str）	        ✅ 直接支持	        ❌
# 字典的键（dict.keys()）	✅ 直接支持	    ❌
# 字典的值（dict.values()）	✅ 需要转换	    ✅ set(dict.values())
# 字典的键值对（dict.items()）	✅ 需要转换	✅ set(dict.items())


# 集合的数学运算：
s = {1, 2, 3}
t = {2, 3, 4}
print("交集 s & t:", s & t)           # 输出: {2, 3}
print("并集 s | t:", s | t)           # 输出: {1, 2, 3, 4}
print("差集 s - t:", s - t)           # 输出: {1}
print("对称差集 s ^ t:", s ^ t)       # 输出: {1, 4}

# 等价的函数方法：
print("intersection:", s.intersection(t))
print("union:", s.union(t))
print("difference:", s.difference(t))
print("symmetric_difference:", s.symmetric_difference(t))
