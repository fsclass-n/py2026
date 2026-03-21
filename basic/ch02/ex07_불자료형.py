# 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.
# True나 False는 파이썬의 예약어로,
# true, false와 같이 작성하면 안 되고 첫 문자를 항상 대문자로 작성해야 한다.
a = True
b = False
# type(x)는 x의 자료형을 확인하는 파이썬의 내장 함수이다.
print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

# 불 자료형은 조건문의 반환값으로도 사용된다.
print(1 == 1) # True
print(2 < 1) # False

# 자료형의 참과 거짓
# "", [], (), {}, 0, None -> False
a = [1, 2, 3, 4]
while a:
    print(a.pop())
# 4
# 3
# 2
# 1

# 불 연산
print(bool('python')) # True
print(bool('')) # False
print(bool([1, 2, 3])) # True
print(bool([])) # False
print(bool(0)) # False
print(bool(3)) # True

# 불 자료형에서는 and, or, not과 같은 논리 연산자를 사용할 수 있다.
# and 연산자는 양쪽 조건이 모두 참일 때만 True를 반환한다.
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# or 연산자는 양쪽 조건 중 하나라도 참이면 True를 반환한다.
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# not 연산자는 참과 거짓을 반대로 바꾼다.
print(not True) # False
print(not False) # True
print(not 1) # False
print(not 0) # True

# 실제 활용 예제
x = 5
y = 10
print(x > 0 and y > 0) # True
print(x > 10 or y > 5) # True
print(not (x > y)) # True

