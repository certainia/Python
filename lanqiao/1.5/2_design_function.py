#                                 函数
# 定义：
# 组织好的，可重复使用的，用来实现单一，或相关联功能的代码段
# 输入参数 --> 函数 --> 返回值

# 格式：
# def 函数名(参数列表):
#     函数体

# 函数的调用：
# 返回值 = 函数名(输入参数)

# example
def Max(a,b):
    if a>b:
        return a
    else:
        return b

bigger = Max(3,5)
biggera = Max(10,8)
print(bigger,biggera)

# problems -- factorial
def Factorial(n):
    sum = 0                      # 初始化sum
    for i in range(1,n+1):
        temp = 1                 # 初始化元素
        while i: 
            temp *= i
            i -= 1               # 自减
        sum += temp            
    return sum                   # 有返回值  返回时打包成一个元组
                                 # 碰到 return 直接结束  没有 return 返回None                                
f1 = Factorial(10) 
print(f1)

# 也可以直接使用单阶乘，然后循环调用函数

# 传参机制
# 形式参数：定义函数时的输入参数
# 实际参数：调用函数诗传递的参数
# 剧本中的角色相当于形参，演员相当于实参
# 在 Python 中，变量本质上是对象的引用（内存地址），
# 所以当你将变量作为参数传递给函数时，实际上是传递了这个对象的引用（地址），而不是对象本身的拷贝

# 值传递：(参数为不可变类型【数字，字符串，元组等】)
def Swap(x,y):
    x, y = y, x 
    print("x:",x, "y:",y)
    print("id(x):",id(x), "id(y):",id(y))

x, y = 3231231, 52141241
print("x:",x, "y:",y)
print("id(x):",id(x) ,"id(y):",id(y)) 
Swap(x,y) 
print("x:",x, "y:",y)
print("id(x):",id(x) ,"id(y):",id(y))

# 引用传递：(参数为可变类型【列表，字典等】)
def F(x):
    x.append(1)
    print(x)
    print(id(x))

x = [1,2,3]
print(x)
print(id(x))

F(x)

print(x)
print(id(x))

# python没有值传递和引用传递这个说法在我看来，就是瞎扯淡，本质是两个的结合，关键是是否可变的指向问题
# 尽量不要传递列表，字典这类可变数据，即使传参，也尽量不要改动【除非就是做处理】，可选择传递副本
# x.copy()  x[:] 都可以创建副本

# 位置参数：
# 实参和形参个数相同，顺序一一对应
def Positional_Argument(a, b, c):
    print(a, b, c)
Positional_Argument(1, 2, 3)  # 1, 2, 3

# 关键字参数
# 根据形参的名字传递参数
def Keyword_Argument(a,b,c):
    print(a,b,c)
Keyword_Argument(b = 2, a = 1, c = 3)
    
# 两者可以混合，但必须保证位置参数在前，关键字参数在后

# 默认参数
# 有默认值的参数必须放到后面,传递时有则改之，无则默认  
def Default_Argument(a,b,c = 3,d = 4,e = 5):
    print(a,b,c,d,e)
Default_Argument(1,2)
Default_Argument(1,2,3)
Default_Argument(1,2,3,4)
Default_Argument(1,2,d = 8)

# 不定长参数
# 可变参数可空，不能有默认值

# 形参前加*表示不定长参数，可以按照位置参数的格式传递多个参数
# 加*的参数会以元组的形式导入，存放所有未命名的变量参数
def Variable_Positional_Argument(a,b,*argtuple):        # 通常写作*args
    print(a)
    print(b)
    print(argtuple)                                     # 元组
Variable_Positional_Argument(1,2,2,3,3)           

# 形参前加**表示不定长参数，可以按照关键字参数的格式传递多个参数
# 加**的参数会以字典的形式导入
def Variable_Keyword_Argument(a,b,**argdict):           # 通常写作**kwargs 
    print(a)
    print(b)
    print(argdict)                                      # 字典
Variable_Keyword_Argument(1,2,c = 3, d = 4)