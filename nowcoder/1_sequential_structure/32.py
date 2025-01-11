import math

a,b,c = map(int,input().split())

x = a+b+c
z = x / 2
y = math.sqrt(z*(z - a)*(z - b)*(z -c))    #记得*连接  而不是数学形式

print(f"circumference={x:.2f}",end=" ")
print(f"area={y:.2f}")