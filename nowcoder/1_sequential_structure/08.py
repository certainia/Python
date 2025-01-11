print("Genius is 1% inspiration and 99% perspiration.")

# # split() 为字符串独有的方法<返回列表对象>：
# 1.默认以空格为分隔符
# s = "hello world python"
# result = s.split()
# print(result)  # 输出: ['hello', 'world', 'python']

# 2.指定即自定义分隔符
# s = "apple,banana,cherry"
# result = s.split(",")
# print(result)  # 输出: ['apple', 'banana', 'cherry']

# 3.指定最大分割次数
# s = "apple,banana,cherry"
# result = s.split(",", maxsplit=1)
# print(result)  # 输出: ['apple', 'banana,cherry']

# 特殊情况
# 1.split() 不会返回空字符串，多个连续分隔符会被视为一个分隔符
# s = "apple,,banana,,,cherry"
# result = s.split(",")
# print(result)  # 输出: ['apple', '', 'banana', '', '', 'cherry']

# 2.空字符串分割时返回空列表
# s = ""
# result = s.split()
# print(result)  # 输出: []

# 3.如果分隔符为 None（不传入参数），会按空白字符分割，并忽略两端和中间多余的空白
# s = "  hello   world  python "
# result = s.split()
# print(result)  # 输出: ['hello', 'world', 'python']

# 4.如果希望结果是元组，可以显式地将列表转换为元组
# values = tuple(input("请输入多个值，用逗号分隔: ").split(","))
# print(values)  # 输出: ('1', '2', '3')
# print(type(values))  # 输出: <class 'tuple'>



# # strip() 为字符串独有的方法<返回字符串对象>：
# # 默认两侧移除
# 1.默认移除空白字符(包括空格_、换行符 \n、制表符 \t 等)
# s = "   hello world   "
# result = s.strip()
# print(result)  # 输出: "hello world"

# 2.自定义移除对象
# s = "xxxyhelloxxx"
# result = s.strip("x")
# print(result)  # 输出: "yhello"

# # 单侧移除
# 1.左侧移除空白
# s = "  hello   "
# result = s.lstrip()
# print(result)  # 输出: "hello   "

# 2.右侧移除空白
# s = "  hello   "
# result = s.rstrip()
# print(result)  # 输出: "  hello"

# 3.左侧移除自定义部分
# s = "yyyhello world"
# result = s.lstrip('y')
# print(result)  # 输出: "hello world"

# 4.右侧移除自定义部分
# s = "hello worldzzzz"
# result = s.rstrip('z')
# print(result)  # 输出: "hello world"



# # just()与center() 为字符串独有的方法<返回字符串对象>：
# 1.左对齐并右侧填充：ljust()
# s = "hello"
# result = s.ljust(10, "-")
# print(result)  # 输出: "hello-----"

# 2.右对齐并左侧填充：rjust()
# s = "hello"
# result = s.rjust(10, "*")
# print(result)  # 输出: "*****hello"

# 3.居中并两侧填充：center()
# s = "hello"
# result = s.center(10, "=")
# print(result)  # 输出: "==hello==="


# # Python的对齐方式:
# 1.左对齐
# text = "Python"
# print(f"{text:<10}")   输出: Python____    

# 2.右对齐
# text = "Python"
# print(f"{text:>10}")   输出: ____Python

# 3.居中对齐
# text = "Python"
# print(f"{text:^10}")   输出: __Python__  

# 4.填充对齐<以居中为例><自然也可以单侧填充>
# text = "Python"
# print(f"{text:*^10}")   输出: **Python**



# # replace() 为字符串对象独有的方法<自然也是返回字符串对象>：
# s = "hello world"
# result = s.replace("world", "Python")
# print(result)  # 输出: "hello Python"



# # + 拼接字符串列表和元组与自定义类：
# 1.拼接字符串
# a = "hello"
# b = "world"
# result = a + " " + b
# print(result)  # 输出: "hello world"

# 2.拼接列表
# list1 = [1, 2]
# list2 = [3, 4]
# result = list1 + list2
# print(result)  # 输出: [1, 2, 3, 4]

# 3.拼接元组
# tuple1 = (1, 2)
# tuple2 = (3, 4)
# result = tuple1 + tuple2
# print(result)  # 输出: (1, 2, 3, 4)

# 4.拼接自定义类
# class CustomList:
#     def __init__(self, items):
#         self.items = items

#     def __add__(self, other):
#         return CustomList(self.items + other.items)

#     def __repr__(self):
#         return str(self.items)

# list1 = CustomList([1, 2])
# list2 = CustomList([3, 4])
# result = list1 + list2
# print(result)  # 输出: [1, 2, 3, 4]


# # map() 是一个高阶函数，用于将指定函数应用到可迭代对象中的每个元素<返回一个迭代器>
# # map(function, iterable, ...)   可以是多个可迭代对象

# 1.单迭代器
# numbers = ["1", "2", "3"]
# result = map(int, numbers)  # 返回一个迭代器
# print(list(result))  # 输出: [1, 2, 3]
# print(result)        # 输出: <map object at 0x0000020047769EA0>则是地址

# 2.多迭代器
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# result = map(lambda x, y: x + y, nums1, nums2)
# print(list(result))  # 输出: [5, 7, 9]

# 特殊情况
# 1.直接调用 map() 返回迭代器
# result = map(int, ["1", "2", "3"])
# print(result)  # 输出: <map object at 0x...>

# 2.迭代器在遍历时才计算结果
# result = map(int, ["1", "2", "3"])
# for r in result:
#     print(r)  # 此时才会逐一计算并输出结果

# 3.迭代器只能遍历一次，如果再次尝试遍历，将不会有结果：
# result = map(int, ["1", "2", "3"])
# print(list(result))  # 第一次: [1, 2, 3]
# print(list(result))  # 第二次: []（空，因为迭代器已经被耗尽）

# 好处：
# 比如：处理大文件： 在逐行处理大文件时，使用惰性求值避免加载整个文件到内存中
# with open("large_file.txt", "r") as f:
#     lines = map(str.strip, f)  # 惰性求值，逐行处理
#     for line in lines:
#         print(line)
        


# # 四舍五入:
# 1.round() 函数可以将浮点数四舍五入到指定的小数位数。

# x = 3.1415926
# print(round(x, 2))  # 输出: 3.14

# 2.如果舍入到整数，可以省略第二个参数：
# print(round(3.1415926))  # 输出: 3



# # 保留小数位数<不管四舍五入，类似于字符串的切片操作>:
# 1.f-string
# x = 3.1415926
# print(f"{x:.2f}")  # 输出: 3.14

# 2.使用 format() 方法
# x = 3.1415926
# print("{:.2f}".format(x))  # 输出: 3.14

# 3.使用 % 格式化
# x = 3.1415926
# print("%.2f" % x)  # 输出: 3.14



# # 从控制台读取输入，并将输入的数据赋值给多个变量:
# 1.通过 split() 方法将输入的字符串拆分成多个部分，并使用解包赋值给多个变量
# 比如读取两个数字<三个同理>
# a, b = input("请输入两个值，用空格分隔: ").split()

# print("第一个值:", a)
# print("第二个值:", b)

# print(type(a))  #读取到与分开的同样是字符串

# 2.分隔输入则不能使用int格式化，虽然可以强转为int，但是麻烦，可以用map来部署
# 以逗号分隔为例
# a, b = map(int,input("请输入两个值，用逗号分隔: ").split(","))

# print("第一个整数:", a)
# print("第二个整数:", b)

# print(type(a))  #分割到的重整为int类型



# # Python 中 *的使用：
# # 序列(列表元组字符串)的重复

# 1.打印分隔线：
# print("-" * 30)     # 输出: ------------------------------

# 2.动态生成图形：
# for i in range(1, 6):
#     print("*" * i)  # 输出: 略

# 3.列表或元组的重复操作(不会深拷贝，只是重复引用):
# print([1, 2] * 3)   # 输出: [1, 2, 1, 2, 1, 2]
# print((1, 2) * 2)   # 输出: (1, 2, 1, 2)

# # 列表元组与字典的解包：
# 1.元组:
# def add(a, b, c):
#     return a + b + c

# args = (1, 2, 3)
# print(add(*args))   # 输出: 6

# 列表:
# args = [4, 5, 6]
# print(add(*args))   # 输出: 15

# 2.字典:
# def show_info(name, age):
#     print(f"Name: {name}, Age: {age}")

# data = {"name": "Alice", "age": 25}
# show_info(**data)   # 输出: Name: Alice, Age: 25

# 3.混合解包：
# def display_info(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")

# 列表解包<位置化参数对应><若为元组应同理>
# args_list = ["Bob", 30, "New York"]
# display_info(*args_list)    # 输出: Name: Bob, Age: 30, City: New York

# 字典解包<关键字传参可以不用注重位置>
# args_dict = {"name": "Carol", "age": 28, "city": "London"}
# display_info(**args_dict)   # 输出：Name: Carol, Age: 28, City: London

# 4.解包字典的键值对<字典的键值可以通过 .items() 遍历并解包>
# data = {"name": "Alice", "age": 25}

# for key, value in data.items():
#     print(key, value)     # 输出:name Alice  换行后 age 25

# 只访问键：使用 keys() 方法返回所有键：
# my_dict = {"a": 1, "b": 2, "c": 3}

# for key in my_dict.keys():
#     print(f"Key: {key}")

# 只访问值：使用 values() 方法返回所有值：
# my_dict = {"a": 1, "b": 2, "c": 3}

# for value in my_dict.values():
#     print(f"Value: {value}")



# 5.更强大的解包
# 列表中的元组
# results = [(1234, 12, 102), (5678, 56, 101), (91011, 91, 101)]

# for i, j, k in results:
#     print(f"{i} = {j} x {k}")

# 列表中的列表
# results = [[1234, 12, 102], [5678, 56, 101], [91011, 91, 101]]

# for i, j, k in results:
#     print(f"{i} = {j} x {k}")
    
# 简单元组中的元组
# results = ((1234, 12, 102), (5678, 56, 101), (91011, 91, 101))

# for i, j, k in results:
#     print(f"{i} = {j} x {k}")

# 嵌套解包
# results = [([1234, 12], 102), ([5678, 56], 101), ([91011, 91], 101)]

# for (i, j), k in results:
#     print(f"{i} = {j} x {k}")



# # 参数解包：
# 1.列表参数解包
# my_list = [1, 2, 3]
# a, b, c = my_list
# print(a, b, c)      # 输出: 1 2 3

# 2.元组参数解包
# my_tuple = (4, 5, 6)
# x, y, z = my_tuple
# print(x, y, z)      # 输出: 4 5 6

# 3.* 可用来捕获多余元素到一个列表中
# numbers = [1, 2, 3, 4, 5]
# a, b, *rest = numbers
# print(a, b, rest)   # 输出: 1 2 [3, 4, 5]

# 4.捕获开头或结尾的多余元素
# *a, b = numbers
# print(a, b)         # 输出: [1, 2, 3, 4] 5

# 5.打包成元组，一般比较高效，相对于列表，元组不可更改并且存储形式单一
# a = 1, 2, 3
# print(a)  # 输出: (1, 2, 3)
# print(type(a))  # 输出: <class 'tuple'>



# 可修改对象：列表 集合 字典
# 不可修改对象：元组 字符串 不可变集合

# 序列：    列表 元组 字符串 范围range    可迭代  支持切片  有序  可通过索引访问  
# 支持序列的很多通用操作：如连接(+)、重复(*)、成员检查(in)、长度(len())等



# # 成员检查<列表 元组 字符串 集合 字典 自定义类>
# 基本语法
# element in sequence      # 检查元素是否在序列中
# element not in sequence  # 检查元素是否不在序列中
# 1.列表成员检查
# my_list = [1, 2, 3, 4, 5]

# print(3 in my_list)  # True
# print(6 in my_list)  # False

# print(6 not in my_list)  # True


# 2.元组成员检查
# my_tuple = ('a', 'b', 'c')

# print('a' in my_tuple)  # True
# print('d' in my_tuple)  # False

# 3.字符串成员检查
# text = "hello world"

# print("hello" in text)  # True
# print("python" in text)  # False

# print("python" not in text)  # True

# 4.集合成员检查<性能更高(哈希表实现)>
# my_set = {10, 20, 30}

# print(10 in my_set)  # True
# print(40 in my_set)  # False

# 5.字典成员检查
# my_dict = {'name': 'Alice', 'age': 25}

# print('name' in my_dict)  # True
# print('name' in my_dict.keys())  # False
# print('Alice' in my_dict.values())

# 6.自定义对象的成员检查<通过实现 __contains__ 方法，支持自定义类的成员检查：>
# class MyContainer:
#     def __init__(self, items):
#         self.items = items

#     def __contains__(self, item):
#         return item in self.items

# my_obj = MyContainer([1, 2, 3])
# print(2 in my_obj)  # True
# print(5 in my_obj)  # False



# # Python中is id == :
# 1.id 用于返回对象的唯一标识（内存地址）
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# 检查对象的 id（内存地址）
# print(id(a))  # 输出 a 的内存地址
# print(id(b))  # b 是 a 的引用，地址相同
# print(id(c))  # c 是新创建的对象，地址不同

# 判断是否是同一对象
# print(id(a) == id(b))  # True
# print(id(a) == id(c))  # False


# 2.== 用于检查两个对象的值是否相等（值相等并不一定是同一个对象）
# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x

# 检查值是否相等
# print(x == y)  # True，因为值相同
# print(x == z)  # True，因为值相同

# 尽管id 返回对象的内存地址，但直接用 is 更方便比较是否是同一对象
# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x

# 3.使用 is 比较
# print(x is z)  # True，因为 x 和 z 指向同一个对象
# print(x is y)  # False，因为 x 和 y 是两个不同的对象

# 温馨提示：小整数、短字符串、布尔值、小元组是常驻对象池的，可能就是直接引用



# len函数内置可直接对可数对象数数,若是类,则可以重写__len__方法自定义类行为
# 同理container容器也是如此,需要重新定义__container__函数



# # Python的内置函数是默认加载的,不需要导入任何模块
# 1.数据类型操作
# len()	返回对象的长度或元素数量
# type()	返回对象的类型
# id()	返回对象的内存地址
# isinstance()	检查对象是否是某一类型的实例
# str()	将对象转为字符串
# int()	将对象转为整数
# float()	将对象转为浮点数
# bool()	将对象转为布尔值
# list()	将对象转为列表
# tuple()	将对象转为元组
# set()	将对象转为集合
# dict()	创建字典或将对象转为字典
# bytes()	将对象转为字节类型

# 2.数学运算
# abs()	返回绝对值
# round()	对数字进行四舍五入
# pow()	幂运算，等同于 x**y
# sum()	求和
# min()	返回最小值
# max()	返回最大值
# divmod()	返回商和余数（元组形式）

# 3.输入输出
# print()	输出内容到控制台
# input()	从用户输入中获取字符串

# 4.迭代与枚举
# range()	生成数字序列
# map()	对可迭代对象的每个元素执行函数
# filter()	筛选出满足条件的元素

# 5.高阶函数
# lambda()	用于创建匿名函数
# sorted()	返回排序后的列表
# reversed()	返回反向迭代器
# eval()	动态执行表达式
# exec()	动态执行代码

# 6.工具函数
# bin()	将整数转换为二进制字符串
# oct()	将整数转换为八进制字符串
# hex()	将整数转换为十六进制字符串
# chr()	返回 Unicode 编码对应的字符
# ord()	返回字符对应的 Unicode 编码
# repr()	返回对象的字符串表示形式


# # 1. 数据类型操作
# print("1. 数据类型操作")

# # len()
# my_list = [1, 2, 3, 4, 5]
# print("列表长度:", len(my_list))

# # type()
# print("类型检查:", type(my_list))

# # id()
# print("对象内存地址:", id(my_list))

# # isinstance()
# print("是否是列表实例:", isinstance(my_list, list))

# # str()
# num = 123
# num_str = str(num)
# print("整数转字符串:", num_str, type(num_str))

# # int()
# num_back = int(num_str)
# print("字符串转整数:", num_back, type(num_back))

# # float()
# float_num = float(num)
# print("整数转浮点数:", float_num, type(float_num))

# # bool()
# print("布尔值:", bool(num))

# # list()
# tuple_data = (1, 2, 3)
# list_data = list(tuple_data)
# print("元组转列表:", list_data)

# # tuple()
# tuple_again = tuple(list_data)
# print("列表转元组:", tuple_again)

# # set()
# set_data = set(list_data)
# print("列表转集合:", set_data)

# # dict()
# dict_data = dict(a=1, b=2, c=3)
# print("创建字典:", dict_data)

# # bytes()
# bytes_data = bytes("hello", encoding="utf-8")
# print("字符串转字节:", bytes_data)      # 字符串转字节: b'hello'

# print("\n2. 数学运算")
# # abs()
# print("绝对值:", abs(-10))

# # round()
# print("四舍五入:", round(3.14159, 2))

# # pow()
# print("幂运算:", pow(2, 3))

# # sum()
# print("求和:", sum([1, 2, 3, 4]))

# # min()
# print("最小值:", min(5, 10, 2))

# # max()
# print("最大值:", max(5, 10, 2))

# # divmod()
# print("商和余数:", divmod(10, 3))    # 商和余数: (3, 1)

# print("\n3. 输入输出")
# # print()
# print("这是输出到控制台的内容")

# # input() （注：这段可能需要手动运行）
# # user_input = input("请输入内容: ")
# # print("您输入的内容是:", user_input)

# print("\n4. 迭代与枚举")
# # range()
# print("生成数字序列:", list(range(1, 10, 2)))

# # map()
# squared = map(lambda x: x ** 2, range(5))
# print("映射平方值:", list(squared))

# # filter()
# even = filter(lambda x: x % 2 == 0, range(10))
# print("筛选偶数:", list(even))

# print("\n5. 高阶函数")
# # lambda
# add = lambda x, y: x + y
# print("匿名函数求和:", add(3, 5))

# # sorted()
# unsorted_list = [5, 2, 9, 1]
# print("排序后的列表:", sorted(unsorted_list))

# # reversed()
# reversed_list = reversed(unsorted_list)
# print("反转后的列表:", list(reversed_list))

# # eval()
# expr = "5 + 10"
# print("动态执行表达式:", eval(expr))

# # exec()
# code = """
# for i in range(3):
#     print(f'动态执行代码: 第{i+1}次')
# """
# exec(code)

# print("\n6. 工具函数")
# # bin()
# print("二进制表示:", bin(10))

# # oct()
# print("八进制表示:", oct(10))

# # hex()
# print("十六进制表示:", hex(10))

# # chr()
# print("Unicode 编码转字符:", chr(97))

# # ord()
# print("字符转 Unicode 编码:", ord('a'))

# # repr()
# print("对象的字符串表示形式:", repr("hello\nworld"))  # 对象的字符串表示形式: 'hello\nworld'

  

# # math函数的补充
# math.ceil(x)	向上取整，返回不小于 x 的最小整数
# math.floor(x)	向下取整，返回不大于 x 的最大整数
# math.trunc(x)	截断小数部分，返回整数部分
# math.factorial(x)	返回 x 的阶乘，x 必须是非负整数
# math.pow(x, y)	返回 x^y，类似 x**y，但更精确
# math.sqrt(x)	返回平方根


