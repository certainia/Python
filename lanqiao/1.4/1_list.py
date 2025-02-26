# 列表的详细操作
# 列表是由一系列按照特定顺序的元素组成的可变数据集合
# 用 [] 定义，各元素之间用逗号隔开，元素类型可以任意

# 定义 --> 访问 --> 修改 --> 增加 --> 删除 --> 查找 --> 排序 --> 反转 --> 遍历 --> 生成 --> 切片 -->拷贝

# 定义列表
ls = [1, 2, 3, 4, 5]


# 访问元素 - 列表有顺序，通过下标进行访问（支持正负下标）
print(ls[0])      # 输出第一个元素：1
print(ls[-1])     # 输出最后一个元素：5
n = len(ls)
print(ls[-n])


# 修改元素 - 列表中的每个元素都可以像普通变量一样使用和修改
ls[1] = 7         # 将下标为1的元素修改为7，ls变为 [1, 7, 3, 4, 5]


# 增加元素：
# append<末尾添加单个元素>
ls.append(6)      # ls变为 [1, 7, 3, 4, 5, 6]

# extend<末尾添加一个可迭代对象中的各个元素>
ls.extend([7, 8]) # ls变为 [1, 7, 3, 4, 5, 6, 7, 8]

# insert<插入元素，从下标0开始计数>
ls.insert(0, 0)   # 在索引0位置插入0，ls变为 [0, 1, 7, 3, 4, 5, 6, 7, 8]


# 删除元素：
# del<关键字，Python自带方法，可以删除指定下标的元素或整个变量>
del ls[-1]        # 删除最后一个元素，ls变为 [0, 1, 7, 3, 4, 5, 6, 7]

# pop<删除并返回指定下标的元素，默认删除最后一个元素>
the = ls.pop()    # 删除最后一个元素并返回，其值赋给变量the，ls变为 [0, 1, 7, 3, 4, 5, 6]
pop_item = ls.pop(2)  # 删除下标为2的元素（值7）并返回，ls变为 [0, 1, 3, 4, 5, 6]

# remove<按照数值删除，删除正序查找到的第一个匹配元素><唯一按照数值删除的><可以加个循环while 也可以for+count删完>
ls.remove(3)      # 删除值为3的第一个元素，ls变为 [0, 1, 4, 5, 6]

# clear<清空列表中的所有元素>
ls.clear()        # ls变为 []


# 重新定义列表用于后续操作
ls = [0, 1, 4, 5, 6]


# 判断元素有无 - in / not in
if 4 in ls:
    print("4在列表中")
if 10 not in ls:
    print("10不在列表中")


# 查找元素：
# count<统计指定元素在列表中出现的次数>
num = ls.count(1)   # 统计1的个数
print(num)

# index<返回指定元素第一次出现的下标>
pos = ls.index(4)   # 查找元素4的下标，若不存在会报错
print(pos)
# index(x, start, end) 可指定查找范围，如：
pos_range = ls.index(4, 0, len(ls))  # 与上面效果相同


# 列表排序：
# sort<原地排序，修改列表本身；reverse参数可选，默认False正序><仅仅list可用>
unsorted_ls = [3, 1, 4, 2]
unsorted_ls.sort()          # 升序排序，unsorted_ls变为 [1, 2, 3, 4]
unsorted_ls.sort(reverse=True)  # 降序排序，unsorted_ls变为 [4, 3, 2, 1]

# sorted<支持所有可迭代对象的排序，返回排序后的新列表><返回列表，set也能排序>
sorted_ls = sorted(unsorted_ls)              # sorted_ls为 [1, 2, 3, 4]
sorted_ls_desc = sorted(unsorted_ls, reverse=True)  # 降序排序

# 字典的键排序
dictionary = {'c': 3, 'a': 1, 'b': 2}
sorted_keys = sorted(dictionary)
print(sorted_keys)  # ['a', 'b', 'c']

# 字典的值排序
sorted_items = sorted(dictionary.items(), key=lambda x: x[1])
print(sorted_items)  # [('a', 1), ('b', 2), ('c', 3)]


# 列表反转：
# reverse<原地反转列表，调用两次可恢复原状><仅仅list可用>
rev_ls = [1, 2, 3, 4, 5]
rev_ls.reverse()     # rev_ls变为 [5, 4, 3, 2, 1]

# reversed<支持所有可迭代对象的反转,返回一个反转的迭代器，需转换为列表或元组>
rev_iter = reversed(rev_ls)         # 返回迭代器
rev_list = list(rev_iter)           # 转换为列表，rev_list为 [1, 2, 3, 4, 5]


# 列表长度 - len<内置函数，可以计算列表中元素个数>
length = len(ls)


# 遍历列表：
# 方式1：使用下标遍历（较麻烦）
for i in range(len(ls)):
    print(ls[i])
# 方式2：直接遍历元素（推荐）
for x in ls:
    print(x)
    
    
# 遍历的同时获取下标 - enumerate<将列表转化为(下标, 元素)形式的元组>
for index, x in enumerate(ls):
    print(index, x)  # 可通过enumerate(ls, start = 你想要的起始下标)设置下标起始值


# 创建数值列表 - 以range为例：
a = list(range(7))          # 生成 [0, 1, 2, 3, 4, 5, 6]
b = list(range(0, 10, 3))     # 生成 [0, 3, 6, 9]


# 列表的拼接与复制：<列表  元组  字符串>
# + 用于拼接两个列表
c = a + b    # 列表c为a和b的拼接结果
# * 用于复制列表
d = a * 4    # 列表d为a重复4次


# 内置函数计算数值：max, min, sum
max_val = max(a)    # 最大值
min_val = min(a)    # 最小值
sum_val = sum(a)    # 总和


# 列表解析式/生成式：
# 基本格式：[表达式 for 变量 in 可迭代对象]
e = [i**2 for i in range(10)]     # 生成0~9的平方列表

# 带条件判断的列表生成式：[表达式 for 变量 in 可迭代对象 if 条件]
f = [i**2 for i in range(10) if i % 2 == 0]  # 仅生成偶数的平方列表

# 多变量生成式，例如使用enumerate或zip：
g = [i * j for i, j in zip(e, f)]  # 对应元素相乘生成新列表,多余的没有
print("g:"+str(g))

# zip 用于将多个可迭代对象按索引对应的元素组合在一起，形成一个新的迭代器，其中每个元素都是一个元组
# 如果输入的可迭代对象长度不同，zip() 会按照最短的序列截断
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]

zipped = zip(a, b, c)  # 生成一个迭代器
print(list(zipped))  # [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# zip 解压
zipped = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
a, b, c = zip(*zipped)

print(a)  # (1, 2, 3)
print(b)  # ('a', 'b', 'c')
print(c)  # (True, False, True)


# 列表切片：
# 格式：[起始:终止:步长]，注意切片不包括终止下标，不会报错
a = [2, 4, 1, 7, 9]
b = a[1:4]       # 得到从下标1到3的子列表，结果为 [4, 1, 7]
b_copy = a[:]    # 切片复制整个列表，相当于拷贝

# 列表的赋值   注意：直接赋值 a_copy = a 是引用赋值，修改其中一个会同步修改
b_copy2 = a.copy()   # 使用copy()方法得到一个浅拷贝 
# 可以直接 b_copy2 = a.copy() 也可以引入头文件copy  b_copy2 = copy.copy(a)

# copy.copy()修改外层不会影响原对象，但修改嵌套对象会影响原对象
# 嵌套的可变对象（如列表、字典）仍然是共享的（修改它们会影响原对象）

# 而直接赋值传递过去则是全会变化
b_copy2 = a   # 即引用赋值，修改其中一个会同步修改

# copy 和 in 适用于所有可迭代对象


# 深入解析
import copy

# 原始列表，内部嵌套一个字典
original = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

# 浅拷贝
shallow_copy = copy.copy(original)

# 修改外层列表（替换元素）
shallow_copy.append({'name': 'Charlie', 'age': 22})
print("原对象:", original)
print("浅拷贝:", shallow_copy)
# 输出：
# 原对象: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
# 浅拷贝: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
# 追加操作仅影响 shallow_copy，原 original 不变

# 修改嵌套字典的内容
shallow_copy[0]['age'] = 26
print("原对象:", original)
print("浅拷贝:", shallow_copy)
# 输出：
# 原对象: [{'name': 'Alice', 'age': 26}, {'name': 'Bob', 'age': 30}]
# 浅拷贝: [{'name': 'Alice', 'age': 26}, {'name': 'Bob', 'age': 30}]
# → 修改 `shallow_copy` 内部的 `dict`，原 `original` 也发生变化


# 解决方法 -->deepcopy
deep_copy = copy.deepcopy(original)

# 修改嵌套字典
deep_copy[0]['age'] = 27
print("原对象:", original)
print("深拷贝:", deep_copy)
# 输出：
# 原对象: [{'name': 'Alice', 'age': 26}, {'name': 'Bob', 'age': 30}]
# 深拷贝: [{'name': 'Alice', 'age': 27}, {'name': 'Bob', 'age': 30}]
# 深拷贝后，修改 deep_copy 的嵌套字典不会影响 original


