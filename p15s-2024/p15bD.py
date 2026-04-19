import sys

T=int(sys.stdin.readline())

for _ in range(T):
    times=sys.stdin.readline()
    year=int(times[:4])
    month=int(times[5:7])
    day=int(times[8:10])
    hour=int(times[11:13])
    minute=int(times[14:16])
    second=int(times[17:19])
    ring_minute=int(times[20:])
    # print(year,month,day,hour,minute,second,)
    unix_time=second+minute*60+hour*3600+(day-1)*86400
    for m in range(1,month):
        if m in [1,3,5,7,8,10,12]:
            unix_time+=31*86400
        elif m in [4,6,9,11]:
            unix_time+=30*86400
        elif m == 2:
            if year%4==0 and year%100!=0 or year%400==0:
                unix_time+=29*86400
            else:
                unix_time+=28*86400
    for y in range(1970,year):
        if y%4==0 and y%100!=0 or y%400==0:
            unix_time+=366*86400
        else:
            unix_time+=365*86400
    #print(unix_time)

    #
    #
    # last_unix_time=unix_time-(unix_time%ring_minute)
    # nyear=1970
    # while True:
    #     is_leap=nyear%4==0 and nyear%100!=0 or nyear%400==0
    #     if last_unix_time<=(366 if is_leap else 365) *86400:
    #         break
    #     else:
    #         nyear+=1
    #         last_unix_time-=(366 if is_leap else 365) *86400
    #
    # is_leap = nyear % 4 == 0 and nyear % 100 != 0 or nyear % 400 == 0
    # nmonth=1
    # days_in_month=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # while True:
    #     sec_in_month=days_in_month[nmonth]*86400
    #     if sec_in_month>last_unix_time:
    #         break
    #     last_unix_time-=sec_in_month
    #     nmonth+=1
    #
    # nday=last_unix_time//86400 + 1
    # last_unix_time%=86400
    #
    # nhour=last_unix_time//3600
    # last_unix_time%=3600
    #
    # nminute=last_unix_time//60
    # nsecond=last_unix_time%60

    # last_ring_time=f'{nyear:04d}-{nmonth:02d}-{nday:02d} {nhour:02d}:{nminute:02d}:{nsecond:02d}'
    last_ring_time=f'{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'
    print(last_ring_time)

