for i in range(1,10):  #第二个乘数因子
    for j in range(1,i+1):   #记得 +1
        if i != 9:
            if j != i: 
                print(f"{j}*{i}={i*j:>2}",end=" ")
            else:
                print(f"{j}*{i}={i*j:>2}")   #既省去了空格，同时换行
        else:
            if j != i:
                print(f"{j}*{i}={i*j:>2}",end=" ")
            else:
                print(f"{j}*{i}={i*j:>2}",end="")   #不换行同时取消空格
                

                
