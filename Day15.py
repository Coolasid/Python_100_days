import time

'''
seconds = time.time()
print(seconds)

local_time = time.ctime(seconds)
print(f"==>> local_time: {local_time}") # Sun Jul 14 08:24:51 2024


# To sleep the current thread
before = time.time()
print('stop the execution for 2 seconds', before)
time.sleep(2)
print('after stopped for 2 seconds', time.time(), time.time() - before)


result = time.localtime()
print('result', result)


result time.struct_time(tm_year=2024, tm_mon=7, tm_mday=14, tm_hour=8, tm_min=26, tm_sec=58, tm_wday=6, tm_yday=196, tm_isdst=0)

current_hour = result.tm_hour

if current_hour < 12:
  print('Good morning')
elif  12 <= current_hour < 18 : 
  print('Good afternoon')
elif 18 <= current_hour < 24:
  print('Good night')

'''

timestamp = time.strftime('%H:%M:%S')
print(f"==>> timestamp: {timestamp}") # ==>> timestamp: 08:43:07
hour = int(time.strftime('%H'))
print(f"==>> hour: {hour}")


if hour < 12:
  print('Good morning')
elif  12 <= hour < 18 : 
  print('Good afternoon')
elif 18 <= hour < 24:
  print('Good night')







