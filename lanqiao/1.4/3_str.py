# 字符串的详细操作

# 1. 基本概念
# Python 中不支持单字符类型，单个字符也是字符串（str）
s1 = "A"   # 这里 "A" 既可以看作一个字符串，也可以视为单个字符



# 2. 字符串的基本操作
# 2.1 访问长度和切片
s = "Hello, Python!"
print(len(s))      # 使用 len() 获取字符串的长度

# 切片操作：与列表类似，格式为 [start:stop:step]，注意可以不包含 stop 下标
print(s[0:5])      # 输出 "Hello"
print(s[-7:])      # 输出 "Python!"（从倒数第7个字符到结尾）


# 2.2 拼接（+）与重复（*）
s2 = "Hello"
s3 = "World"
print(s2 + " " + s3)  # 使用 + 连接字符串，结果为 "Hello World"
print(s2 * 3)         # 使用 * 重复字符串，结果为 "HelloHelloHello"


# 2.3 in 与 not in 及类型转换
if "Pyt" in s:
    print("包含 'Pyt'")
if "Java" not in s:
    print("不包含 'Java'")

# 类型转换：利用 str() 将其他类型转换为字符串
num = 100
s_num = str(num)      # s_num 为 "100"



# 3. 转义字符与字符串的书写
# 转义字符使用反斜杠 (\) 表示，常见的有：
#   \n  换行符
#   \t  制表符（横向制表符）
#   \\  反斜杠本身
#   \'  单引号
#   \"  双引号

# 行尾的 \ 可以用于续行，不会引入额外的换行符：
s_multi = "fanhengjia\
NB"  # 这里的 \ 将两行连接成一行，s_multi 的值为 "fanhengjiaNB"
print(f"使用\\t制表符:\t{s_multi}")
print(f"使用\\t\\t制表符:\t\ts")   # \t 会产生水平制表符的效果



# 4. ord() 与 chr() 函数
# ord(字符) 返回字符对应的 Unicode 码点
# chr(码点) 将 Unicode 码点转换为对应的字符
x = ord("蓝")
y = ord("桥")
print("蓝的 Unicode 编码:", x)
print("桥的 Unicode 编码:", y)

# 反过来用 chr() 得到字符
m = chr(x)
n = chr(y)
print(m, n)   # 输出 "蓝 桥"



# 5. 字符串的判断类方法（通常以 is 开头，返回布尔值）
s_alpha = "HelloWorld"
print(s_alpha.isalnum())   # True，判断字符串是否仅包含字母（a-zA-Z）和数字（0-9）
print(s_alpha.isalpha())   # True，判断所有字符是否均为字母（识别 Unicode 字符中的“字母”）(也可以混合)
print("12345".isdigit())   # True，判断是否全部为数字
print("hello".islower())   # True，判断是否全部为小写字母
print("HELLO".isupper())   # True，判断是否全部为大写字母
print("   \n\t".isspace())  # True，判断是否全部为空白字符（空格、换行、制表符）
print("Title Case".istitle())  # True，判断每个单词首字母是否大写，其余字母小写



# 6. 字符串的转换类方法（原字符串不变，返回新字符串）
s_mixed = "python programming"
print(s_mixed.title())    # 将每个单词首字母大写，结果 "Python Programming"
print(s_mixed.upper())    # 全部转换为大写 "PYTHON PROGRAMMING"
print(s_mixed.lower())    # 全部转换为小写 "python programming"
print("Hello World".swapcase())  # 大小写互换，结果 "hELLO wORLD"


# 去除空白或指定字符：
s_space = "   hello   "
print(s_space.lstrip())   # 删除左侧空白，结果 "hello   "
print(s_space.rstrip())   # 删除右侧空白，结果 "   hello"
print(s_space.strip())    # 删除两边空白，结果 "hello"
# 即不修改原本字符串


# 替换字符串中的内容：
s_replace = "I like Python, Python is fun."
# replace(原字符串, 新字符串, [最大替换次数]) —— 注意 replace 返回新字符串
print(s_replace.replace("Python", "Java"))             # 替换所有 "Python" 为 "Java"
print(s_replace.replace("Python", "Java", 1))          # 仅替换第一个 "Python"
print(s_replace)                                       # 原有的保持不变
# 即不修改原本字符串


# 字符串的对齐方法：
s_align = "Center"
print(s_align.ljust(10))           # 左对齐，宽度为10，默认用空格填充，结果 "Center    "
print(s_align.rjust(10))           # 右对齐，宽度为10，结果 "    Center"
print(s_align.center(10, "-"))     # 居中对齐，宽度为10，使用 '-' 填充，例如 "—Center—"
# 注意：ljust, rjust, center 均返回新字符串，不修改原字符串



# 7. 字符串的查找方法
s_search = "hello, hello, hello"
# count：统计子字符串出现的次数
print(s_search.count("hello"))   # 输出 3

# index：类似 find，但未找到时会抛出 ValueError 异常
print(s_search.index("hello"))   # 输出第一次出现 "hello" 的索引位置

# find：查找子字符串第一次出现的位置，未找到返回 -1,范围同样可选
print(s_search.find("lo"))       # 输出 "lo" 第一次出现的索引位置
print(s_search.find("abc"))      # 未找到，返回 -1

# 若使用 index 查找不存在的子字符串，则会报错，故实际使用中建议用 find()  <list tuple 不支持>



# 8. 字符串的拆分与拼接
s_split = "apple,banana,cherry"
# split：按照指定分隔符拆分字符串，返回列表
fruits = s_split.split(",")    # 结果 ['apple', 'banana', 'cherry']
print(fruits)
# 可指定 maxsplit 参数限制拆分次数
fruits_max = s_split.split(",", maxsplit=1)   # 结果 ['apple', 'banana,cherry']
print(fruits_max)

# join：将可迭代对象中的字符串(必须是字符串)按指定分隔符连接成一个新字符串
joined = "-".join(fruits)      # 结果 "apple-banana-cherry"
print(joined)



# 9. 字符串的“修改”方法
# 由于字符串不可变，若需“修改”字符串，可以采用以下方式：
# 方式一：转换为列表，再修改后用 join 拼接回字符串
s_mod = "hello"
lst = list(s_mod)         # 转换为列表 ['h', 'e', 'l', 'l', 'o']
lst[0] = 'H'              # 修改第一个字符
s_mod_new = "".join(lst)  # 重新拼接为 "Hello"
print(s_mod_new)

# 方式二：利用切片和拼接构造新字符串
s_mod2 = "hello"
s_mod2_new = "H" + s_mod2[1:]  # 将首字母替换为大写
print(s_mod2_new)

# 方式三：使用 replace 方法（适合替换子字符串）
s_mod3 = "hello world"
s_mod3_new = s_mod3.replace("world", "Python")
print(s_mod3_new)



# 10. 字符串格式化
name = "dafds"
age = 19

# 使用 format() 方法进行格式化：
# 10.1 无参数占位，按顺序填充
formatted1 = "{}{}".format(name, age)
print(formatted1)

# 10.2 带索引占位符
formatted2 = "{0}{1}{1}{0}{0}".format(name, age)
print(formatted2)

# 10.3 带名称占位符
formatted3 = "{name}{age}".format(name="dafds", age=19)
print(formatted3)

# 除了 format() 之外，在 Python 3.6+ 中还可使用 f-string 格式化（更直观）
formatted4 = f"{name} is {age} years old."
print(formatted4)
# 可以写入变量  数学表达式  函数调用 列表 字典索引 三目运算符 生成式 join拼接字符串 不用eval

# 格式化时也可指定数字的宽度、精度等，例如：
pi = 3.14159265
print("Pi 的值是：{:.2f}".format(pi))   # 输出 "Pi 的值是：3.14"
print(f"Pi 的值是：{pi:.3f}")            # 使用 f-string 格式化，输出 "Pi 的值是：3.142"