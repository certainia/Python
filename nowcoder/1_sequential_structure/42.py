import math
a,b,c = map(int,input().split())

x = math.sqrt(a*c//b)
y = math.sqrt(a*b//c)
z = math.sqrt(b*c//a)

print(int(4*(x+y+z)))