# 전 세계의 파이썬 고수들이 만든 유용한 프로그램을 모아 놓은 것이 바로 파이썬 표준 라이브러리
# 파이썬 표준 라이브러리는 파이썬을 설치할 때 자동으로 컴퓨터에 설치된다.
# datetime.date, time, math.gcd, math.lcm, random, itertools.zip_longest,
# itertools.permutations, itertools.combinations, functions.reduce,
# operator.itemgetter, shuitl, glob, pickle, os, zipfile, threading,
# tempfile, traceback, json, urllib, webbrowser

# datetime.date
# datetime.date는 연, 월, 일로 날짜를 표현할 때 사용하는 함수
import datetime
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,4,5)
# day2에서 day1을 빼면 datetime 모듈의 timedelta 객체가 반환된다.
diff = day2 - day1
print(diff.days) # 477

# 요일은 datetime.date 객체의 weekday 함수를 사용하면 쉽게 구할 수 있다.
day = datetime.date(2021, 12, 14)
# 0은 월요일을 의미하며 순서대로 1은 화요일, 2는 수요일, …, 6은 일요일
print(day.weekday()) # 1
# 월요일은 1, 화요일은 2, …, 일요일은 7을 반환하게 하려면
# isoweekday 함수를 사용하면 된다.
print(day.isoweekday()) # 2

# time
# time.time
# time.time()은 UTC(universal time coordinated, 협정 세계 표준시)를 사용하여
# 현재 시간을 실수 형태로 반환
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환
import time
print(time.time()) # 1774367134.4515128

# time.localtime
# time.localtime은 time.time()이 반환한 실숫값을
# 연, 월, 일, 시, 분, 초, ... 형태로 바꾸어 주는 함수
print(time.localtime(time.time()))
# time.struct_time(tm_year=2026, tm_mon=3, tm_mday=25, tm_hour=0,
# tm_min=46, tm_sec=36, tm_wday=2, tm_yday=84, tm_isdst=0)

# time.asctime
# time.asctime은 time.localtime이 반환한 튜플 형태의 값을 인수로 받아서
# 날짜와 시간을 알아보기 쉬운 형태로 반환
print(time.asctime(time.localtime(time.time())))
# Wed Mar 25 00:47:39 2026

# time.ctime
# time.asctime(time.localtime(time.time()))은
# 간단하게 time.ctime()으로 표시할 수 있다.
# ctime이 asctime과 다른 점은 항상 현재 시간만을 반환한다는 점이다.
print(time.ctime()) # Wed Mar 25 00:48:29 2026

# time.strftime
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는
# 여러 가지 포맷 코드를 제공한다.
# time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
import time
print(time.strftime("%x", time.localtime(time.time())))
# 03/25/26
print(time.strftime("%c", time.localtime(time.time())))
# Wed Mar 25 00:50:07 2026

# time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다.
# 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.
# 1초 간격으로 0부터 9까지의 숫자를 출력한다.
import time
for i in range(10):
    print(i)
    time.sleep(1)

# 인수 없이 time 함수 사용하기
print(time.localtime()) # time.struct_time(tm_year=2026, tm_mon=3, tm_mday=25, tm_hour=0, tm_min=53, tm_sec=33, tm_wday=2, tm_yday=84, tm_isdst=0)
print(time.asctime()) # Wed Mar 25 00:53:33 2026
print(time.strftime('%c')) # Wed Mar 25 00:53:33 2026