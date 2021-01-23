import time
# 获取时间戳
t = time.time()
print(t)
t_local =time.localtime(t)      # 当前时间
print(t_local)
T = time.strftime("%Y/%m/%d %H:%M:%S",t_local)   # 时间格式化
print(T)
t_array = time.strptime(T,"%Y/%m/%d %H:%M:%S")
Tstamp = time.mktime(t_array)
print(int(Tstamp))
# 时间转时间戳：time.time() ->  time.strptime() -> time.mktime() 时间->时间数组->时间戳
print('-'*50)
import datetime as dt

localtime = dt.datetime.now()   # 返回当前时间
print(localtime)

# 时间格式化最有效的办法
strf = localtime.strftime("%Y/%m/%d  %H:%M:%S ")
print(strf)










