a, b = map(int,input().split())
temp = divmod(a,b)
for i in range(2):
    print(temp[i],end=" ")
