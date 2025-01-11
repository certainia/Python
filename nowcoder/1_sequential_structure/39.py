temp = map(int,input().split())

temp = sorted(temp)

print(abs(temp[3]+temp[0]-temp[1]-temp[2]))   # 加个绝对值