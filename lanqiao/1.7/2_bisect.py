# bisect —— 数组二分查找算法

# bisect 模块：维护一个已排序列表，支持二分查找、二分插入

# bisect_left(a, x, lo=0, hi=len(a)):
#   □ 查找有序列表 a 中，插入元素 x 的第一个位置
#   □ 如果 a 中存在元素 x，返回第一个 x 的位置
#   □ 如果 a 中不存在，则返回该出现的位置


import bisect

a = [1, 2, 4, 4, 5, 6]
x = 4

pos = bisect.bisect_left(a, x)
print(pos)  # 2（4 第一次出现的位置）

x = 3
pos = bisect.bisect_left(a, x)
print(pos)  # 2（3 应该插入到索引 2）



# bisect_right(a, x, lo=0, hi=len(a)):
#   □ 查找有序列表 a 中，插入元素 x 的最后一个位置
#   □ 如果 a 中存在元素 x，返回最后一个 x 的位置 + 1
#   □ 如果 a 中不存在，则返回该出现的位置


a = [1, 2, 4, 4, 5, 6]
x = 4

pos = bisect.bisect_right(a, x)
print(pos)  # 4（4 最后出现的位置 +1）

x = 3
pos = bisect.bisect_right(a, x)
print(pos)  # 2（3 仍然应该插入索引 2）



# bisect 模块：维护一个已排序列表，支持二分查找、二分插入

# insort_left(a, x, lo=0, hi=len(a)):
#   □ 查找有序列表 a 中，在第一个位置插入元素 x 保持有序


a = [1, 2, 4, 4, 5, 6]
x = 4

bisect.insort_left(a, x)
print(a)  # [1, 2, 4, 4, 4, 5, 6]（在第一个 4 之前插入）

x = 3
bisect.insort_left(a, x)
print(a)  # [1, 2, 3, 4, 4, 4, 5, 6]



# insort_right(a, x, lo=0, hi=len(a)):
#   □ 查找有序列表 a 中，在最后一个位置插入元素 x 保持有序


a = [1, 2, 4, 4, 5, 6]
x = 4

bisect.insort_right(a, x)
print(a)  # [1, 2, 4, 4, 4, 5, 6]（在最后一个 4 之后插入）

x = 3
bisect.insort_right(a, x)
print(a)  # [1, 2, 3, 4, 4, 4, 5, 6]

# 后两个参数直接省略即可
