str1 = "hello world"

for i in range(len(str1)):  # 动态获取字符串长度
    
    print(chr(ord(str1[i]) + 1), end="")
