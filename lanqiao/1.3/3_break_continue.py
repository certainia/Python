# break 与 continue 
# break 语句可以跳出for和while的循环体
# continue 表示跳出当前语句循环体的剩余语句，然后进行下一步循环

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)     # output : 4,3  
           
    # 对比continue
    
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)     # output  : 4,3,1,0
