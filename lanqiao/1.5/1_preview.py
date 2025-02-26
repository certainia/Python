# eval()函数

# 将传入的字符串解析为 Python 表达式。
# 运行该表达式并返回结果。
# 如果表达式无效或存在语法错误，则会抛出异常。

result = eval("(lambda x: x**2)(4)")
print(result)  # 输出: 16

# or

print("4+2*9")


# int-float  除法结果自然一定是float
# int和float进行比较时int自动转为float，可以有math.isclose(a,b)逼近比较



# 猴子补丁 
def Sum(a, b):
    print("调用原始的 Sum 函数")
    return a + b

def NewSum(*args):
    print("调用新的 NewSum 函数")
    return sum(args)

# 替换原函数
Sum = NewSum

# 调用 Sum 实际调用的是 NewSum
result = Sum(1, 2, 3, 4, 5)
print(result)  # 输出: 15
 
# 1. 原始的 Sum 函数被新的 NewSum 函数替换
# 2. 所有调用 Sum 的地方，实际上都会调用 NewSum



# 如果本地作用域中找不到变量
# Python 会查找是否在外层函数的作用域中定义（适用于嵌套函数）
# 嵌套函数可以访问外层函数的变量，但不能直接修改（除非使用 nonlocal 关键字）
def outer_function():
    outer_var = "I am in enclosing scope"

    def inner_function():
        print(outer_var)  # 可以访问外层函数变量

    inner_function()

outer_function()

# 使用 nonlocal 修改外层函数变量:

def outer_function():
    outer_var = "Original value"

    def inner_function():
        nonlocal outer_var  # 声明为外层变量
        outer_var = "Modified value"

    inner_function()
    print(outer_var)  # 输出：Modified value

outer_function()


# 变量作用域
# 局部变量：函数内部的变量，仅作用于函数内部
# 全局变量：函数外部的变量，作用于全局

total = 0
def f(a,b):
    # print(total)   # 此处即为错误，即变量未定义
    total = a + b
    print(total)     # total仅作用于里面，覆盖掉外面的total
f(10,20)
print(total)

# 如何在函数内部使用全局变量 --> 使用global声明
total = 0
def f(a,b):
    global total     # 用global做全局声明，仅在本代码块作全局声明
    print(total)     # 没问题 
    total = a+b
    print(total)     # total实现了共享
f(10,20)
print(total)



# Python:
# result = "偶数" if x % 2 == 0 else "奇数"
# c/c++:
# result = (x % 2 == 0) ? "偶数" : "奇数";