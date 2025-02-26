                            # 基本输入输出
# print输出函数
# 语法：print(*objects,sep=' ',end='\n')

# 默认以空格分割(sep)，默认以换行结尾(end)
print("Hello","World",123)
print("Hello","World",123)
print("Hello","World",123)

print()

print("Hello","World",123,sep='+') 
print("Hello","World",123,sep='-')
print("Hello","World",123)

print()

print("Hello","World",123,end="apple")
print("Hello","World",123,end='?')
print("Hello","World",123)

a = 1
b = 'runoob'
print(a,b)

print()

print("aaa""bbb")            # 字符串的连接
print("aaa""bbb",sep=',')    # 连接之后sep分隔一定是不凑效的，字符串直接跨引号连上
print("aaa","bbb",sep=',')           # 这样可以

# 应用
print("www","lanqiao","cn",sep='.')