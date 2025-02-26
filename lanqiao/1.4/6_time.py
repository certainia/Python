# time 模块

# time.time()：获取当前系统时间戳（浮点数类型，单位秒）
# time.sleep(seconds)：让程序暂停执行指定的秒数
# time.localtime()：将时间戳转换为本地时间（返回 time.struct_time 对象）
# time.strftime(format, t)：将 time.struct_time 或类似对象格式化为字符串
# time.strptime(string, format)：将字符串解析为 time.struct_time


import time

# 获取当前时间戳
current_timestamp = time.time()
print("当前时间戳:", current_timestamp)

# 将当前时间戳转为本地时间（struct_time对象）
local_t = time.localtime(current_timestamp)
print("本地时间struct_time:", local_t)

# 将本地时间格式化输出
time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_t)
print("格式化时间:", time_str)

# 暂停执行2秒
time.sleep(2)
print("暂停2秒后继续执行...")


# datetime.date

# date.today()：获取当前本地日期
# date(year, month, day)：手动创建一个日期对象
# isoformat()：将日期对象转换为 YYYY-MM-DD 的字符串
# strftime(format)：自定义格式化输出

from datetime import date

# 获取今天的日期
today = date.today()
print("今天日期:", today)          # 例如：2025-02-10
print("年:", today.year)          # 2025
print("月:", today.month)         # 2
print("日:", today.day)           # 10
print("星期：",today.weekday())

# 创建自定义日期
d = date(2023, 12, 31)
print("自定义日期:", d)

# 日期格式化输出
print("ISO格式:", d.isoformat())                  # '2023-12-31'
print("自定义格式:", d.strftime("%Y/%m/%d"))       # '2023/12/31'



# datetime.time

# time(hour, minute, second, microsecond=0, tzinfo=None)：创建一个纯时间对象
# isoformat()：返回 HH:MM:SS 或带微秒的字符串
# strftime(format)：自定义格式化输出

from datetime import time

# 创建一个时间对象
t = time(14, 30, 45, 123456)  # 时、分、秒、微秒
print("时间对象:", t)                 # 14:30:45.123456
print("小时:", t.hour)                # 14
print("分钟:", t.minute)              # 30
print("秒:", t.second)                # 45
print("微秒:", t.microsecond)         # 123456

# 时间格式化输出
print("ISO格式:", t.isoformat())       # '14:30:45.123456'
print("自定义格式:", t.strftime("%H:%M:%S"))  # '14:30:45'


# datetime.datetime

# datetime.now()：获取当前本地日期时间
# datetime(year, month, day, hour, minute, second, microsecond=0, tzinfo=None)：创建一个日期时间对象
# strftime(format)：自定义格式化输出
# strptime(string, format)：从字符串解析得到日期时间对象
# isoformat()：返回 ISO 标准格式字符串（如 2025-02-10T14:30:45.123456）

from datetime import datetime

# 获取当前本地日期时间
now = datetime.now()
print("当前日期时间:", now)     # 例如：2025-02-10 15:00:00.123456

# 创建自定义日期时间
custom_dt = datetime(2023, 12, 31, 23, 59, 59)
print("自定义日期时间:", custom_dt)

# 格式化输出
print("ISO标准:", custom_dt.isoformat())  
print("自定义格式:", custom_dt.strftime("%Y-%m-%d %H:%M:%S"))

# 字符串解析为 datetime
dt_str = "2023-12-31 23:59:59"
parsed_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
print("从字符串解析得到:", parsed_dt)
print(type(parsed_dt))


# timedelay

# timedelta 代表时间间隔（差值），内部存储的核心单位是天（days）、秒（seconds）和微秒（microseconds），
# 而我们通常在创建它时可以通过以下关键字参数指定：
# days、seconds、microsecondsmilliseconds、   minutes、hours、weeks (Python 会自动转换为天、秒、微秒)

import datetime
from datetime import timedelta
# 三个属性

td = timedelta(days=2, hours=3, minutes=15, seconds=30, microseconds=500000)

print("天数:", td.days)  # 2
print("秒数:", td.seconds)  # 11730 (3小时 + 15分钟 + 30秒)
print("微秒:", td.microseconds)  # 500000 (即 0.5 秒)

# 单个方法total_seconds()<返回整个 timedelta 换算成总秒数(包括天数转换)>

td = timedelta(days=2, hours=3, minutes=15, seconds=30)
print("总秒数:", td.total_seconds())  # 183330.0
# (2天 × 86400秒) + (3小时 × 3600秒) + (15分钟 × 60秒) + 30秒 = 183330 秒


# 示例：为某个日期加减天数
from datetime import date, timedelta

# 假设有一个指定日期
d = date(2025, 2, 10)
print("原始 date:", d)  # 2025-02-10

# 加 7 天
d_plus_7 = d + timedelta(days=7)
print("加7天:", d_plus_7)  # 2025-02-17

# 减 3 天
d_minus_3 = d - timedelta(days=3)
print("减3天:", d_minus_3)  # 2025-02-07



# 示例：为某个日期时间加减小时、分钟
from datetime import datetime, timedelta

# 假设有一个指定日期时间
dt = datetime(2025, 2, 10, 22, 15, 30)
print("原始 datetime:", dt)  
# 2025-02-10 22:15:30

# 加 2 小时
dt_plus_2h = dt + timedelta(hours=2)
print("加2小时:", dt_plus_2h)  
# 2025-02-10 00:15:30（可能跨到次日的 00:15:30，具体要看时区，这里只是演示）

# 减 30 分钟
dt_minus_30m = dt - timedelta(minutes=30)
print("减30分钟:", dt_minus_30m)
# 2025-02-10 21:45:30

# 要想在“纯时间”的基础上做加减，需要给它配一个日期来构成完整的 datetime，再进行运算
from datetime import date, time, datetime, timedelta

# 一段纯时间
t = time(22, 15, 30)
print("原始 time:", t)

# 先给它“配”一个日期（例如今天），得到完整 datetime
today_date = date(2025, 2, 10)
dt = datetime.combine(today_date, t)  
# dt = 2025-02-10 22:15:30

# 开始做加减运算
dt_plus_90m = dt + timedelta(minutes=90)
print("加 90 分钟:", dt_plus_90m)
# 2025-02-11 00:45:30 (若跨到次日)

# 如果只关心新的 time 部分
new_time = dt_plus_90m.time()
print("新的 time:", new_time)  
# 00:45:30



# 计算时间差（相减得到 timedelta）
# date - date

from datetime import date

d1 = date(2025, 2, 10)
d2 = date(2025, 2, 20)

delta_date = d2 - d1
print("两个 date 相差:", delta_date)     # 10 days, 0:00:00
print("相差天数:", delta_date.days)       # 10

# datetime - datetime
from datetime import datetime

dt1 = datetime(2025, 2, 10, 22, 15, 30)
dt2 = datetime(2025, 2, 13, 1, 15, 30)

delta_dt = dt2 - dt1
print("两个 datetime 相差:", delta_dt)  
# 2 days, 3:00:00 (示例：差 2天3小时)

print("相差天数:", delta_dt.days)       
# 2
print("相差秒数:", delta_dt.seconds)    
# 10800 (3 小时 = 10800 秒)
# 直接 time - time 同样不支持，会报 TypeError。
# 要比较两个时间点的先后差值，可以先将它们分别结合日期转成 datetime，再相减。


