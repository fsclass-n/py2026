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