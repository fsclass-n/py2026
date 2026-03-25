# 오류는 언제 발생하는가?
# 1. 존재하지 않는 파일을 열려고 할 때 발생하는 오류이다.
# f = open("나없는파일", 'r')
# FileNotFoundError:
# [Errno 2] No such file or directory: '나없는파일'

# 2. 0으로 다른 숫자를 나누는 경우
# 4 / 0
# ZeroDivisionError: division by zero

# 3. 인덱스 오류
a = [1, 2, 3]
# a[3]
# IndexError: list index out of range

# 예외 처리 기법
# try-except 문
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
# 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.
# try:
#   ...
# except [발생오류 [as 오류변수]]:
#   ...

try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # division by zero

# try-finally 문
# finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
# 보통 finally 절은 사용한 리소스를 close해야 할 때 많이 사용한다.
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.
    # (... 생략 ...)
finally:
    f.close() # 중간에 오류가 발생하더라도 무조건 실행된다.

# 여러 개의 오류 처리하기
# try:
#     ...
# except 발생오류1:
#     ...
# except: 발생오류2:
#     ...
# 인덱싱 오류가 먼저 발생했으므로
# 4 / 0에 따른 ZeroDivisionError 오류는 발생하지 않는다.
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e) # list index out of range

# ZeroDivisionError와 IndexError를 함께 처리할 수도 있다.
try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e) # list index out of range

# try-else 문
# try:
#     ...
# except [발생오류 [as 오류변수]]
#     ...
# else: # 오류가 없을 경우에만 수행
#     ...
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')