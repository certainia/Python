import math

results = []

def judging(k):
    
    # 将 i, j, k 拼接成字符串
    digits = str(i) + str(j) + str(k)
    
    # 检查是否正好包含1~9的所有数字 且 不重复
    return len(digits) == 9 and set(digits) == set("123456789")  # 集合的无序性

    
for i in range(1000,10000):
    for j in range(1,int(math.sqrt(i))+1):
        if i % j == 0:
            k = i // j
            if judging(k):
                results.append((i,j,k)) # 三元组(元组)一样使用，同样是列表的可迭代对象
                
# 三元组遍历
for i,j,k in results:
    print(f"{i} = {j} x {k}")