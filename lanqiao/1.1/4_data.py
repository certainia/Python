
                            # 常量和变量
# 常量：程序中使用的具体的数值,字符,运行过程中无法修改
# 变量：表示一个存储单元，其中存储的值可以改变
# 命名规则：1>只能包含字母，数字，下划线  2>不能以数字开头  #3> 不可用关键字



                            # 基本数据类型
# 整数int 浮点数float 字符串str 布尔bool 获取变量类型type()                                              

# 整数int的运算，涉及到除法，结果化为浮点数
# 浮点数float的运算可能不准确，无限逼近
# 字符串可以通过+连接（元组，列表也可），
# 如果要强行连接，可以用str()函数强转，四种数据类型都可以自由转换
# 布尔类型即True False

# int转float：直接转化
# float转int：舍弃小数
# int转bool：0：False  其他：True
# bool转int：False:0   True:1
# str：直接转

a = int(-1.4)
b = int(-1.7)
c = int(-1.5)

print(a,b,c)  # 小数部分直接全部舍弃


a = 1.9999999 + 0.0001
print(int(a))    # 保证浮点数的正确输出实现


a = False 
print(type(a))

a = int(a)
print(type(a))