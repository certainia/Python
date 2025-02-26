                            # while 循环
# 求1-n的和:
summ = 0
n = int(input())
while(n):
    summ += n
    n = n - 1
print(summ)

summm = sum(range(n+1))  # 简单
summmm = n*(n+1)/2       # 更简单


# 于个人看来，while循环处理不计数的好一些，同时算是自带了判断语句

# example
# s = 1 + 2 + 3 + 4 + ………… +n,当 s>1000时，n最小是多少
s = 0
n = 1
while s <= 1000:
    s += n
    n += 1
print(n - 1)                # 切忌是n - 1  <另解：循环体的两条语句互换，但要修改初始化>   



# 转转相除法 gcd(m,n) = gcd(n,m % n)  条件：m > n
m = int(input())
n = int(input())
if m < n :
    m,n = n,m
r = m % n                   # 余数需要用得到，所以保留一下

while r != 0: 
    m = n
    n = r
    r = m % n

print(n)