# # 字典（dict）的详细操作

# # 字典存储一系列的键值对，键必须为不可变类型（数字、字符串、元组），值可以为任意类型
# # 字典使用 {} 创建；空字典同样使用 {}（与空集合的定义区分开来）

# # 1. 字典的定义和创建
# # 1.1 使用 {} 直接创建
# dic1 = {'a': 1, 'b': 2, 'c': 3}
# print("dic1:", dic1)

# # 1.2 使用 dict() 构造字典
# dic2 = dict(a=1, b=2, c=3)
# print("dic2:", dic2)

# # 1.3 通过 zip() 函数将两个序列组合成字典
# keys = ['a', 'b', 'c', 'd', 'e']
# values = [1, 2, 3, 4, 5]
# zipped = zip(keys, values)     # 毕竟zip返回的是迭代器
# dic3 = dict(zipped)
# print("dic3 (通过 zip 创建):", dic3)

# # 注意：zip() 返回的是一个迭代器，迭代后会耗尽，
# # 若需多次使用可先转换为列表：
# zipped_list = list(zip(keys, values))
# print("转换后的列表:", zipped_list)
# print("通过列表构造字典:", dict(zipped_list))


# # 2. 字典的访问与修改
# # 2.1 访问：使用 dic[key]，若 key 不存在会抛出 KeyError
# print("dic3['a']:", dic3['a'])
# # 使用 get() 方法可以设置默认值，若 key 不存在则返回 None 或指定默认值
# print("dic3.get('f'):", dic3.get('f'))
# print("dic3.get('f', '默认值'):", dic3.get('f', '默认值'))
# print("dic3.get('f', '默认值'):", dic3.get('a', '默认值'))


# # 2.2 添加或修改字典
# # 如果键已存在则修改对应的值，否则添加新的键值对
# dic3['a'] = 100   # 修改已有键 'a'
# dic3['f'] = 6     # 添加新的键 'f'
# print("更新后的 dic3:", dic3)


# # 3. 字典的删除操作
# # 使用 del 关键字删除指定键及其对应的值
# dic_temp = {'语文': 99, '数学': 88}
# print("原字典:", dic_temp)
# del dic_temp['语文']
# print("使用 del 删除 '语文':", dic_temp)


# # 使用 pop() 方法删除键并返回其对应的值
# # 若键不存在，可指定默认值，否则会抛出 KeyError
# dic_temp['英语'] = 75
# pop_value = dic_temp.pop('英语', None)
# print("pop() 删除 '英语' 返回的值:", pop_value)
# print("删除 '英语' 后的字典:", dic_temp) 


# # 4. 字典的遍历
# dic_sample = {'a': 1, 'b': 2, 'c': 3}
# # 4.1 遍历字典时，默认遍历的是字典的键
# for key in dic_sample:
#     print("遍历得到的键:", key)

# # 4.2 使用 keys() 遍历所有键
# for key in dic_sample.keys():
#     print("keys() 遍历键:", key)

# # 4.3 使用 values() 遍历所有值
# for value in dic_sample.values():
#     print("values() 遍历值:", value)

# # 4.4 使用 items() 遍历所有键值对，返回二元组
# for key, value in dic_sample.items():
#     print("items() 遍历: 键 =", key, "值 =", value)
    
# # 也可以直接遍历 items() 得到元组
# for item in dic_sample.items():
#     print("遍历到的元组:", item)


# # 5. 字典的其他操作
# # 5.1 判断键、值或键值对是否存在
# print("'a' in dic_sample:", 'a' in dic_sample)   # 检查键是否存在
# print("1 in dic_sample.values():", 1 in dic_sample.values())  # 检查值是否存在
# print("('a', 1) in dic_sample.items():", ('a', 1) in dic_sample.items())


# # 5.2 字典的复制
# # 直接赋值只是引用，修改其中一个会影响另一个
# dic_reference = dic_sample          # 引用赋值
# dic_shallow = dic_sample.copy()     # 浅拷贝
# import copy
# dic_deep = copy.deepcopy(dic_sample)  # 深拷贝（适用于嵌套字典）


# # 5.3 字典的合并
# # 使用 update() 方法将一个字典的键值对合并到另一个字典中，
# # 若有重复的键，则后面的会覆盖前面的
# dic_a = {'a': 1, 'b': 2}
# dic_b = {'b': 3, 'c': 4}
# dic_a.update(dic_b)
# print("合并后的 dic_a:", dic_a)


# # 5.4 字典推导式（字典解析式）
# # 快速构造字典的一种方式，类似于列表生成式
# squares = {x: x**2 for x in range(1, 6)}
# print("字典推导式 squares:", squares)

# # 字典推导式
# keys = ['name', 'age', 'gender']
# values = ['Alice', 25, 'Female']
# info = {k: v for k, v in zip(keys, values)}
# print(info)
# # {'name': 'Alice', 'age': 25, 'gender': 'Female'}

# # 同样的方法
# keys = ['name', 'age', 'gender']
# values = ['Alice', 25, 'Female']
# info = dict(zip(keys, values))
# print(info)

# # map 详解 
# # map(function, iterable)
# # function：要应用的函数（可以是内置函数、lambda 匿名函数或自定义函数）
# # iterable：可迭代对象（如 list、tuple）
# # 返回值：返回 map 迭代器（需要用 list() 或 tuple() 转换才能看到结果）

# # filter 详解 
# # filter(function, iterable)
# # function：返回布尔值的函数（True 保留，False 过滤掉）
# # 返回值：返回 filter 迭代器（需要用 list() 或 tuple() 转换）
# # 示例
# numbers = [1, 2, 3, 4, 5, 6]

# # 先筛选偶数，再求平方
# result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))

# print(list(result))  # 输出: [4, 16, 36]

# # 常见的可迭代对象<可迭代对象都可以用于 for 循环或 list(), tuple() 转换>
# # 数据类型	    示例	    是否可变
# # 列表（list）	[1, 2, 3]	✅ 可变
# # 元组（tuple）	(1, 2, 3)	❌ 不可变
# # 字符串（str）	"hello"	    ❌ 不可变
# # 集合（set）	{1, 2, 3}	✅ 可变
# # 字典（dict）	{"a": 1, "b": 2}	✅ 可变
# # range 对象	range(5)	❌ 不可变
# # 迭代器（Iterator）	iter([1, 2, 3])	✅ 可变（遍历后耗尽）
# # 生成器（Generator）	(x for x in range(3))	✅ 可变（遍历后耗尽）

# # 元组是不可变的，但如果它包含列表或字典，这些内部对象仍然是可变的。
# # 虽然可以修改元组中可变对象的内容，但不能改变元组的结构

# # 生成器
# # 生成器表达式 比 列表推导式 更节省内存：
# # 列表推导式（会生成完整列表，占用更多内存）
# lst = [x ** 2 for x in range(10**6)]

# # 生成器表达式（不会占用大量内存）
# gen = (x ** 2 for x in range(10**6))
# # 适用于大规模数据处理，因为它不会一次性创建整个列表，而是逐步计算数据。

# # # 简单示例
# def my_generator():
#     print("生成器开始执行")
#     yield 1  # 生成第一个值
#     print("继续执行")
#     yield 2  # 生成第二个值
#     print("继续执行")
#     yield 3  # 生成第三个值
#     print("生成器结束")

# gen = my_generator()  # 创建生成器

# print(next(gen))  # 生成 1
# print(next(gen))  # 生成 2
# print(next(gen))  # 生成 3

# # # 输出
# # # 生成器开始执行
# # # 1
# # # 继续执行
# # # 2
# # # 继续执行
# # # 3
# # # 生成器结束

