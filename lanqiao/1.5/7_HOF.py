# functool
# Functools模块应用于高阶函数，即参数/返回值为其他函数的函数
# 我们仅学习偏函数：partial
# 即“冻结”某些函数的参数或关键字参数，然后返回一个函数

# sorted(iterable,[,key = 函数]) 
# example
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['apple', 'banana', 'cherry'] （按长度排序）

 
# functools.partial(func, *args, **keywords)

# func：需要被扩展的函数，返回的函数其实是一个类 func 的函数

# *args：需要被固定的位置参数

# **kwargs：需要被固定的关键字参数
def poww(x,y):
    return x ** y

from functools import partial

square = partial(poww, y = 2)  # None 代表占位，调用时必须提供第一个参数
print(square(3))  # 9
print(square(4))  # 16




# 高阶函数
# 函数可以作为参数传递给另一个函数  / 函数可以作为返回值返回
# 1.高阶函数 --> map()  filter()  reduce()  sorted()
# 2.装饰器闭包常用
def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)  # 返回的是 inner 函数
cube = power(3)

print(square(5))  # 25 (5²)
print(cube(2))    # 8  (2³)