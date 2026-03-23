# 입력값과 반환값의 존재 유무에 따라 4가지 유형
# 1. 일반적인 함수
# 입력값이 있고 반환값이 있는 함수가 일반적인 함수이다.
# def 함수_이름(매개변수):
#   수행할_문장
#   ...
#   return 반환값

def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

# 함수의 사용법
# 반환값을_받을_변수 = 함수_이름(입력_인수1, 입력_인수2, ...)

# 2. 입력값이 없는 함수
def say():
    return "Hi"

# 반환값을_받을_변수 = 함수_이름()
a = say()
print(a)

# 3. 반환값이 없는 함수
def add(a, b):
    print("%d, %d의 핪은 %d입니다." % (a, b, a + b))

# 함수_이름(입력_인수1, 입력_인수2, ...)
add(3, 4)

a = add(3, 4)
# None은 값이 없음을 나타내는 객체이다.
# 참과 거짓을 따질 때는 False처럼 동작한다.
print(a) # None

# 4. 입력값도, 반환값도 없는 함수
def say():
    print('Hi')

# 함수_이름()
say()

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result) # 4

# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다
result = sub(b=5, a=3)
print(result)  # -2
