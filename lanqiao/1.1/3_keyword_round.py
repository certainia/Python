# Python保留字/关键字

# 获取关键字
import keyword
print(keyword.kwlist)
print(f"Total keywords: {len(keyword.kwlist)}")
print()
# 布尔值：True  False  None
# 流程控制：if elif else   for while break continue pass   try except finally raise 
# 逻辑运算：and  or  not  is  in
# 定义与声明：def class lambma   import from as   glabal nonlocal assert del
# 异步编程：async await  函数返回与生成器：return yield  上下文管理：with
# NAN为浮点数，表示“非数字”，通常用于表示未定义或不可表示的数值（例如 0/0）


# java/c的round函数: + :floor(x + 0.5)   - :ceil(x - 0.5)
# python的round函数：银行家策略，取离.5最近的偶数     不是.5，则向最近的整数靠近  

print(round(2.5))
print(round(-2.5))
print(round(3.5))
print(round(-3.5))

print()

print(round(2.4))
print(round(2.6))

print()

# round的四舍五入
# round(number, ndigits)
print(round(2.536,2))
