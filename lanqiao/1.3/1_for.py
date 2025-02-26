                    # for循环
# range函数用于生成一系列的数字，用于循环结构的遍历
# python3生成的是可迭代对象(可遍历的)

# 语法:range(start,stop,step)  每一个参数传入一个整数
# start默认为0，step默认为1，左闭右开区间
# range(5)  ==  range(0,5)  ==  range(0,5,1) 
# range(10,-1,-2)  == (10,8,6,4,2,0)


# for语句：for <variable> in <sequence>
#             <循环变量 i,j,k> <序列或可迭代对象 range(xx)>
# 循环次数即遍历元素个数

# example
# 输入一个整数n，求1-n的所有偶数
n = int(input())
for i in range(2,n+1,2):
    print(i,end=' ')   # 思路一 <还可以步长为1，判断输出>
    
# 输入一个整数n，计算1 + 2 + 3 + ……………… + n的和
sum = 0
n = int(input())
for i in range(1,n+1):
    sum += i
print(sum)             # 其实这种从0开始即可，即range(n+1)

# 输入一个整数n,计算n的阶乘
mul = 1
n = int(input())
for i in range(n,0,-1):
    mul *= i 
print(mul)              # 可以 mul = 1 ，range从1开始  <如下代码所示>
                        # 可以 mul = n ，range从n - 1开始   xxx --> 未考虑0 
                        # 最后设定end = 0 ,0! = 1 ,1! = 1
mul = 1
n = int(input())
for i in range(1,n+1):
    mul *= i
print(mul)              # 这个更合适一点

# 输入一个整数n，分别计算奇偶数和
sum1 = sum2 = 0
n = int(input())
for i in range(1,n+1):
    if i % 2 == 0:
        sum2 += i
    else:
        sum1 += i
print(sum1,sum2)          # 直接暴力算

sum1 = sum2 = 0
n = int(input()) 
sum1,sum2 = sum(range(1,n+1,2)),sum(range(2,n+1,2))
print(sum1,sum2)          # 调用函数算

import math
sum1 = sum2 = 0
n = int(input()) 
sum1 = (math.floor((n+1)/2)) ** 2
sum2 = (math.floor(n/2)) * (math.floor(n/2) + 1)   # 重点
print(sum1,sum2)


