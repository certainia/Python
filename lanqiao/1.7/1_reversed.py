# 自定义排序
# sorted(iterable, key=None, reverse=False): 返回一个排序后的结果
# iterable —— 可迭代对象。
# key —— 主要用于比较元素，只接受一个参数，参数是可迭代对象中的元素，key 函数的返回值用于排序
# reverse —— 排序规则：reverse=True —— 降序排序  reverse=False —— 升序排序（默认）

# sorted 只是创建了一个副本 不改变原有的状态
a = [1, 3, 2, 5, 4]

sorted_a = sorted(a)
print("a = ", a)
print("sorted_a = ", sorted_a)

sorted_a = sorted(a, reverse=True)
print("sorted_a = ", sorted_a)


# 自定义排序   key = func 
# 字符串长度
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['date', 'apple', 'cherry', 'banana']

# 绝对值大小
nums = [-10, 5, -3, 2, -8]
sorted_nums = sorted(nums, key=abs)
print(sorted_nums)  # [2, -3, 5, -8, -10]

# 特定顺序排序
pairs = [(1, "banana"), (3, "apple"), (2, "cherry")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(3, 'apple'), (1, 'banana'), (2, 'cherry')]

# 多个条件排序
people = [("Alice", 25), ("Bob", 30), ("Charlie", 25), ("David", 35)]
sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
print(sorted_people)
# [('Alice', 25), ('Charlie', 25), ('Bob', 30), ('David', 35)]
# 即 key=lambda x: (x[1], x[0]) 先按年龄（x[1]）排序，若相同则按名字（x[0]）排序



# 写函数自定义
from functools import cmp_to_key

# 自定义规则："a<b 返回负数"，"a>b 返回正数"，"二者相等返回 0"
# 自定义规则："当a排序值在前面返回负数"，"当b排序值在前面返回正数"，"二者相等返回 0"
def cmp(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        if a <= b:            # ASCII 排序
            return -1
        else:
            return 1

a = ["Python", "Swift", "Java", "C++", "Go", "Rust"]
sorted_a = sorted(a)
print("按照默认排序: ", sorted_a)

sorted_a = sorted(a, key=cmp_to_key(cmp))
print("按照自定义排序: ", sorted_a)