# input 输入函数
# 语法：input([prompt])

a = input()        # 假设本次输入abc 
print(a,type(a))   # input 输入的东西都是str字符串类型

a = input()        # 假设本次输入123
print(a,type(a))   # type(……) 求……的类型

a = int(input())   # 假设本次输仍然输入123
print(a,type(a))   # int()嵌套强转为int类型


a = input("Please input:")   # 先一步打印输出然后打印到终端提示输出
print(a,type(a))   # 比赛不要打印，但是要知道

# 含有字符比如数字加字符  自然就当字符串处理了



# 练习

# 已知三角形三边输入a,b,c ；求三角形面积(根据海伦公式)
# 补充: p = (a+b+c)/2   S = p(p-a)(p-b)(p-c).sprt()  input读入输入的一整行信息

a = int(input())
b = int(input())
c = int(input())

p = (a+b+c)/2
print((p*(p-a)*(p-b)*(p-c))**(1/2))  # 1/2 记得加括号 或者0.5



# 输入两个正整数a,b，计算a+b,a-b,a*b,a/b,a^b

a = int(input())
b = int(input())

# 以分隔的方式模拟换行输出
print(a+b,a-b,a*b,a/b,a**b,sep="\n") 



# 从a时b开始游泳，c时d分结束，输出一个整数表示游泳时长

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(c*60 + d - a*60 - b)