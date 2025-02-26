# if 语句   <英文冒号 + 代码块缩进>
# 语法：if 表达式：
#           代码块 

# if-else 语句   <if else 对齐 + else后无物>
# 语法：if 表达式：
#           代码块 
#       else:
#           代码块2

# 同样支持嵌套<无须举例>

# 筛出偶数
a = int(input())
if a % 2 == 0:
    print(a)
else:
    pass

# 排序
a = int(input())
b = int(input())
if a>b:
    pass
else:
    a,b = b,a
print(a,b)

# if-elif-else 语句
# 语法：if 表达式：
#           代码块 
#       elif:
#           代码块2
#       elif:
#           代码块3
#       elif:
#           …………
#       else:
#           代码块n

# 模三取余
a = int(input())
if a % 3 == 0:
    print("a就是3的倍数")
elif a % 3 == 1:
    print("a对3取余为1")
else:
    print("a对3取余为2")
    
    
# 分类顺序结构
# 即满足一个就跳出判断了
a =  int(input())
if a < 10:
    print(1)
elif a < 100:
    print(2)
elif a < 1000:
    print(3)
else:
    print(4)

# 例题分析:有钱n，三物品单价4，5，6，尽量买多并且不留钱
a,b,c = 0,0,0
n = int(input())
if n % 4 == 0:
    a = n // 4
elif n % 4 == 1:
    a = n // 4 
    a -= 1
    b += 1
elif n % 4 == 2:
    a = n // 4 
    a -= 1
    c += 1
else:
    a = n // 4
    b += 1
    c += 1

# 求闰年(两种格式)
a = int(input())
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
         print("Yes")
else:
    print("No")
    
    
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Yes")
else:
    print("No")