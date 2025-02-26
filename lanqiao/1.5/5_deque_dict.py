# 双端队列deque
# deque只接受一个可迭代对象

# 更新了三个左侧操作
# append appendleft
# extend extendleft
# pop popleft

# 更新了rotate右循环  rotate(n)

from collections import deque
a = deque([1,2,3,4])
print(a)
a.rotate(2)
print(a)
a.rotate(-2)
print(a)



# 带默认值的字典 defaultdict
# 也是为了简便  省去get的默认值操作 
from collections import defaultdict

d = defaultdict(int)
print(d['x'])


# 用处
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = defaultdict(int)
for word in words:
    count[word] += 1  # 直接加 1，不需要判断是否存在
print(count)


d = defaultdict(list)
print(d['x'])

d = defaultdict(set)
print(d['x'])

d = defaultdict(dict)
print(d['x'])


# example
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)
# defaultdict(list) 能够直接使用 append() 方法，而普通的 dict 不能
print(d)
# 不然就要用d[k] = d.get(k,0) + 1



# 有序字典
# 对于原始字典 -->
data = [('a', 1), ('b', 2), ('c', 3)]
d = dict(data)

print(d)
while len(d) != 0:
    print("删除的元素为：", d.popitem())
    print("d = ", d)
# 仅能删除最后一个

# 对于有序字典 
from collections import OrderedDict

data = [('a', 1), ('b', 2), ('c', 3)]
d = OrderedDict(data)

d.popitem(last=False)   # 删尾
d.popitem(last=True)    # 删首
d.popitem(2)            # 删除索引为2的元素
print(d)

data = [('a', 1), ('b', 2), ('c', 3)]
d = OrderedDict(data)
d.move_to_end('c',last=False)    # 挪动到左侧
print(d)
d.move_to_end('c',last=True)     # 挪动到右侧
print(d)