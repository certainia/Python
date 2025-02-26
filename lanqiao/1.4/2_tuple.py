# 元组的详细操作
# 元组是由一系列按照特定顺序的元素组成的不可变数据集合
# 用 () 定义，元素之间用逗号隔开，一旦创建便不能修改


# 定义元组
tpl = (1, 2, 3, 4, 5)


# 访问元组元素 - 同列表，通过下标访问（支持正负下标）
print(tpl[0])    # 输出第一个元素：1
print(tpl[-1])   # 输出最后一个元素：5


# 元组不可修改 - 以下操作会报错：
# tpl[1] = 7   # TypeError: 'tuple' object does not support item assignment


# 元组的方法较少，但也提供了常用的两个方法：
# count<统计指定元素在元组中出现的次数>
num_tpl = tpl.count(2)   # 统计元素2出现的次数
print(num_tpl)
# index<返回指定元素第一次出现的下标>
pos_tpl = tpl.index(3)   # 获取元素3的下标
print(pos_tpl)


# 遍历元组：
for x in tpl:
    print(x)
for index, x in enumerate(tpl):
    print(index, x)


# 元组切片 - 同列表，返回新的元组
tpl_slice = tpl[1:4]     # 结果为 (2, 3, 4)


# 元组的拼接与重复：
tpl2 = (6, 7)
tpl_concat = tpl + tpl2   # 拼接元组，结果为 (1, 2, 3, 4, 5, 6, 7)
tpl_repeat = tpl * 2      # 重复元组，结果为 (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)


# 内置函数同样适用于元组：
max_val_tpl = max(tpl)    # 求元组中的最大值
min_val_tpl = min(tpl)    # 求元组中的最小值
sum_val_tpl = sum(tpl)    # 求元组中所有元素的和


# 元组虽然不可修改，但可以通过转换为列表进行修改，再转换回元组：
tpl_list = list(tpl)   # 转换为列表
tpl_list[0] = 0        # 修改列表中元素
tpl_modified = tuple(tpl_list)  # 转换回元组，结果为 (0, 2, 3, 4, 5)
print(tpl_modified)


# 反转元组：
# 方法1 - 利用切片（推荐）
tpl_reversed = tpl[::-1]   # 得到反转后的元组

# 方法2 - 使用reversed()函数，并转换为元组
tpl_reversed2 = tuple(reversed(tpl))