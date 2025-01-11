temp = int(input())

a = temp // 3600
b = temp % 3600 // 60       # 两个// 代表求商
c =  temp % 60

print(a,end=" ")
print(b,end=" ")
print(c,end="")