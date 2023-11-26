import datetime

t = 2

t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"

t1_segundos = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
t2_segundos = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
print(str(int(abs((t1_segundos - t2_segundos).total_seconds()))))