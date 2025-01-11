a = int(input())

b = pow(a,1/3)

c = 3*b

# print(round(c,3))  # 若是小数位后为0，浮点数默认省略，所以这样不准 
print(f"{c:.3f}")

