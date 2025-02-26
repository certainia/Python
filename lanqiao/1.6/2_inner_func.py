# 内置方法
# 查询函数  查询函数功能
help(divmod)      

# 执行字符串表达式，返回表达式的结果
x = 4
y = eval("x+2+3") 

# 转化为16/8/2进制
m = hex(12)
n = oct(12)
o = oct(12)

# 序列 和 集合操作
len()             # 求长度函数 
sorted()          # 排序函数
reversed()        # 翻转函数
zip()             # 组合可迭代对象
enumerate()       # 枚举
range()           # 生成数字序列

# 类型转换和处理
int()
float()
bool()
str()
list()
tuple()
set()
dict()
type()
id()
chr()
ord()

# 其他常用
# 查看函数或模块名称的详细说明
help() 
help(print)  # 查看 print() 函数的帮助信息
help(str)    # 查看 str 类型的帮助信息

# 判断所有可迭代对象是否全为True
all()
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([]))                   # True（空可迭代对象返回 True）
print(all([1, 2, 3]))            # True（所有非零数都是 True）
print(all([0, 1, 2]))            # False（0 代表 False）

# 判断所有可迭代对象是否有一个为True
any()
print(any([False, False, True]))  # True（因为有一个 True）
print(any([False, False, False])) # False（全为 False）
print(any([]))                     # False（空可迭代对象返回 False）
print(any([0, 0, 1]))              # True（1 代表 True）

# 获取当前范围内的属性列表
dir()
print(dir())  # 获取当前作用域的变量、函数等
print(dir(str))  # 查看字符串对象的所有方法

# 判断对象是否存在属性
hasattr()
class Person:
    name = "Alice"

p = Person()
print(hasattr(p, "name"))  # True
print(hasattr(p, "age"))   # False

# 返回对象的属性值
getattr()
class Person:
    name = "Alice"

p = Person()
print(getattr(p, "name"))  # Alice
print(getattr(p, "age", "No Attribute"))  # 如果属性不存在，返回 "No Attribute"

# 输入
input()
# 输出
print()
# 生成迭代器
iter()
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # 抛出 StopIteration 错误

# 迭代器下一个
next()

# 可迭代对象（Iterable）：

# 具备 __iter__() 方法，支持 for 循环。
# 但它不是迭代器，不会自动保存遍历状态，每次遍历都从头开始。
# 例子：list、tuple、dict、set、str、range 等。

# 迭代器（Iterator）：

# 具备 __iter__() 和 __next__() 方法，调用 next() 获取下一个元素。
# 只能遍历一次，用完后就失效。
# 例子：map、filter、zip 这些返回的对象，以及 iter(可迭代对象) 生成的迭代器。

# 序列作映射
map()
nums = [1, 2, 3, 4]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # [1, 4, 9, 16]






# 数学操作函数
# 绝对值函数
abs()
# 四舍五入函数
round()
# 求和函数
sum()
# 最大值
max()
# 最小值
min()
# 幂次
pow()
# 构建复数 
complex()
# 返回商和函数
divmod()
