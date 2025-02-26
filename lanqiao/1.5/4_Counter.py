                            # collections库
# Counter统计
a = ["apple", "banana", "apple", "cat", "cat", "cat", "cat", "dog"]
b = {}

# 方法 1
for x in a:
    b[x] = b.get(x, 0) + 1
print(b)

# 方法 2
from collections import Counter
c = Counter(a)
print(c)


# 定义方式：
# Counter(可迭代对象)
# Counter(字典)
from collections import Counter   # ---可以直接视为字典

a = Counter()  # 空Counter
a = Counter('Hello World')  # 统计每个字符出现次数
a = Counter([1,2,3,1,2])  # 统计每个元素出现次数

# 利用字典初始化每个元素(key)和出现次数(value)
a = Counter({'a':1, 'b':2, 'c':3})
a = Counter(a=1, b=2, c=3)          # 此行同上做法


# example
# 操作集：most_common(k)  elements()  clear()
from collections import Counter
a = Counter('Hello world')
print(a)
print(a.keys())
print(a.values())
print(a.most_common(2))
print(a.elements())
print(list(a.elements()))
 
 
# 操作集  +  -  &  |
c = Counter(a=3, b=1)
d = Counter(a=2, b=2)

print("c + d =", c + d)
print("c - d =", c - d)
print("c & d =", c & d)
print("c | d =", c | d)

# +（加法）： 两个 Counter 相加，合并相同键的值
# -（减法）： 相减后，删除结果中小于等于 0 的键
# &（交集）： 取两个 Counter 中相同键的最小值
# |（并集）： 取两个 Counter 中相同键的最大值