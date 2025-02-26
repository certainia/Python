                                  # 循环嵌套
# 两种循环的区别:
# for 循环：常见用于循环次数已知的情况，或者遍历list，dict等数据结构 <1+2+3+……+99>
# while 循环：不知道循环次数，但可以根据终止条件终止循环 <s>1000 与 辗转相除法>

# 双重循环<外循环和内循环> 可以看作外部循环的变量已知
# break仅仅跳出单层循环，可以设定一个表示在内层循环外控制外层循环的跳出


# example
# 求s = 1! + 2! + 3! + 4! + 5! + ……………… + n!
s = 0
n =  int (input())
for i in range(1,n+1):
    sum = 1      # 每次初始化
    while i:     # 内层for循环亦可
        sum *= i
        i -= 1
    s += sum
    
print(s)

# example
# 500块钱买鸡,买了90只，已知母鸡15，公鸡10，小鸡5
count = 0
for i in range(91):
    for j in range(91):
        for k in range(91):
            count += 1   
            if i + j + k == 90 and 15 * i + 10 * j + 5 * k == 500:
                print(i,j,k)    # 暴力解法，费时费力
print()
    
count = 0    
for i in range(500//15):
    for j in range(min(500//10,90 - i)):
        k = 90 - i - j
        count += 1
        if 15 * i + 10 * j + 5 * k == 500:
            print(i,j,k)        # 算法求解，省时省力
print()

for i in range(6):  # 推出来的范围
    j = 10 - 2 * i
    k = 80 + i 
    print(i,j,k)                # 数学求解，两个方程可以表示三个未知数
print()   
    
    
    
    
n = 4    
# 直角三角形画图
for i in range(1,n + 1):        # 涉及到次数的一般就要有1
    for j in range(i):
        print("*",end='')       # 或者是"*" * i，更优
    print()                     # 勿忘
print()       
        
for i in range(1,n+1):
    for j in range(1,2 * n - 1 + 1):
        if j == n - i + 1 or j == n - 1 + i :     # 终极公式 n-(i-1)   n+(i-1)
            print("*",end='')
        else:
            print(" ",end='')          # 空心三角
    print()
            
for i in range(1,n+1):
    for j in range(1,2 * n - 1 + 1):
        if j >= n - i + 1 and j <= n - 1 + i:     # and不是or
            print("*",end='')
        else:
            print(" ",end='')            # 实心三角 
    print()
            
# 画出菱形的话 根据曼哈顿距离求解  曼哈顿距离 vs 欧几里得距离
# 空心菱形
def hollow_diamond(n):
    for i in range(-(n-1), n):
        for j in range(-(n-1), n):
            # 判断 (i, j) 是否刚好在曼哈顿距离 == n-1 的位置
            if abs(i) + abs(j) == n - 1:
                print("*", end='')
            else:
                print(" ", end='')
        print()  # 换行
        
# 实心菱形
def solid_diamond(n):
    # i, j 同时从 -(n-1) 到 n-1
    for i in range(-(n-1), n):
        for j in range(-(n-1), n):
            # 判断 (i, j) 是否在曼哈顿距离 < n 的区域内
            if abs(i) + abs(j) < n:
                print("*", end='')
            else:
                print(" ", end='')
        print()  # 换行


# example <三位水仙花数>
for m in range(100,1000):
    sum = 0
    i,j,k = map(int, str(m))                # NB i,j,k = str(m) 这样的话是str  序列解包，字典的话解包是键
    sum += pow(i,3) + pow(j,3) + pow(k,3)
    if sum == m:
        print(sum)

# example  <输出m-n素数>
import math
m = int(input())
n = int(input())
for i in range(m,n+1):
    flag = True
    for j in range(2,math.sqrt(i)+1):
        if i % j == 0:
            flag = False
            break
        # 1 既不是素数 也不是合数
    if flag and i != 1:
        print(i)           
            
