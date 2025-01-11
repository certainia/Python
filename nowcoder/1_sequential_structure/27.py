a = input().split()

temp = 0

for i in a:
    temp += int(i)    # 记得强转

temp = temp/5

print(f"{temp:.1f}")