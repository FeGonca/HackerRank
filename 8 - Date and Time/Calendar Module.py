# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

m, d, y = map(int, input().split())

num_dia = calendar.weekday(y, m, d)
nome_dia = calendar.day_name[num_dia]

print(nome_dia.upper())