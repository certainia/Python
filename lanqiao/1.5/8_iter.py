                            # 迭代器 itertools   
# 生成长度为无限的迭代器
# count(start=0, step=1)：创建一个迭代器，它从 start 值开始，返回均匀间隔的值
# cycle(iterable)：创建一个迭代器，循环遍历 iterable 中所有元素
# repeat(object[, times])：创建一个迭代器，如果没有指定 times 则无限循环遍历 object

from itertools import count,cycle,repeat

for x in count(start = 0, step = 1):
    print(x)
    if x > 1000:   
        break
    
count = 0
for i in cycle("hello"):                            
    print(i)
    count += 1
    if count > 300:
        break

for a in repeat("hello",100):
    print(a)



# 有限迭代器
# accumulate(iterable[, func])：创建一个迭代器，返回累积汇总值或其他双目运算函数的累积结果值

# accumulate([1,2,3,4,5]) → 1 3 6 10 15
# accumulate([1,2,3,4,5], max) → 1 2 3 4 5
# accumulate([1,2,3,4,5], operator.mul) → 1 2 6 24 120

# chain(*iterables)：合并多个迭代器

# chain('ABC', 'DEF') → A B C D E F   # 区别zip

from itertools import accumulate,chain
a = [1,2,3,4,5]
b = list(accumulate(a))
print(b)                          # --> 求前缀和

a = [3,1,2,4,5]
b = list(accumulate(a,max))
print(b)

a = [3,1,2,4,5]
b = list(accumulate(a,min))
print(b)

import operator
a = [3,1,2,4,5]
b = list(accumulate(a,operator.mul))
print(b)

for x in chain('ABC','def'):  # 参数个数不限制
    print(x,end = ' ')
print()



# 排列组合迭代器
# 可迭代对象的笛卡尔积product()
# product(*iterables,[,repeat]) repeat限制维度
from itertools import product
x = product([1,2,3],[4,5,6])
y = product([3,4,5],repeat = 2)  # == product([3,4,5],[3,4,5])

# 排列组合迭代器
from itertools import permutations,combinations
# 排列   --> r可选(因为设置了默认值为最大)
# itertools.permutations(iterable, r)
# 从 n 个元素中选出 r 个元素，并考虑顺序的所有可能情况,按照从小到大的顺序
a = list(permutations([1,2,3,4]))
print(a)

print() 

# 组合   --> r必选
# itertools.combinations(iterable, r)
# 从 n 个元素中选出 r 个元素，不考虑顺序
a = list(combinations([1,2,3,4],r = 3))
print(a)