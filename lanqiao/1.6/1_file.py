# 类：   （类型），自定义各种类型用于对应现实生活，例如 student 类、teacher 类等
# 对象： （变量），类的实例化，用类创建的具体对象
class Student:  # class + 类名 + 冒号
    # 属性
    x = "hello"
    
    # 初始化方法，初始化一个对象
    def __init__(self,name,class_idx):
        self.name = name
        self.class_idx = class_idx
    
    def output(self):  # 类里面定义函数都要这个 self 不然无法获取内部信息
        print("打印当前对象的内部信息")
        print(self)
        print(self.name,self.class_idx)
        
# 传参：初始化几个参数传递几个参数，不考虑self
A = Student("小明","一班")
print(A.name,A.class_idx)
B = Student("小王","二班")  
print(B.name,B.class_idx)
B.output()

# __init__(self)：构造函数（构造方法）
# 可以包含多个参数，但必须包含 self 参数。
# self 必须作为第一个参数。
# self 不需要手动传递参数。

# 类的实例化
# 格式： 类名(参数)，这里传入的参数会被传递给 __init__ 构造函数。


# 类属性（类变量）：在类体中，所有函数外定义的变量。
# 使用方式： 类名.变量名

# 实例属性（实例变量）：以 self.变量名 形式定义的变量。
# 使用方式：
# 实例名.变量名
# self.变量名（在类的方法内部使用）

# 类的属性和类中函数同等级的 
# 类的属性直接用类直接调用
# 所有的对象公用一个类的属性

class Teacher():
    sex_list = ["boy","girl"] 
    
    @classmethod
    def get_sex_list(cls):      # cls 类似于 对象方法的 self
        return cls.sex_list
    
    @staticmethod
    def test():
        print("Hello!")
    
print(Teacher.get_sex_list())   # 同类属性的调用（前）/对象方法的调用（后）         
print(Teacher.test())           # 基本同类方法，无须传特殊（cls/self）参，无法获取类属性和类方法

# 魔法函数/方法的重写