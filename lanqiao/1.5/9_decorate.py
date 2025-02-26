# 闭包是指在一个函数内部定义另一个函数，并且内嵌函数引用了外层函数的变量
# 当外层函数执行完毕后，其局部变量通常会被销毁，但被内嵌函数捕获的变量会一直保留，供后续调用时使用

# example
def outer_function(x):
    def inner_function(y):
        return x + y  # 内嵌函数使用了外层变量 x
    return inner_function

closure = outer_function(10)
print(closure(5))  # 输出 15，因为内嵌函数记住了 x=10



# 装饰器是一种特殊的闭包，它接受一个函数作为参数，返回一个新的函数，
# 用以扩展或修改原函数的行为，而不需要改变原函数的源代码

# 基本结构
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # 在这里可以添加额外的功能（前置操作）
#         result = func(*args, **kwargs)
#         # 这里可以添加后置操作
#         return result
#     return wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("装饰器开始工作")
        result = func(*args, **kwargs)
        print("装饰器工作结束")
        return result
    return wrapper

@my_decorator  # 等价于：say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello, world!")

say_hello()

# 闭包 使得内嵌函数可以记住并访问其定义时的环境，从而保持状态
# 装饰器 则是利用闭包机制对函数进行包装，在执行前后增加额外的逻辑，实现代码的复用和扩展
