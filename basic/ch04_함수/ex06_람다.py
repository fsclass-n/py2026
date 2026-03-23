def add(a, b):
    return a + b

result = add(3, 4)
print(result) # 7

# lambda(람다) 예약어
# 함수를 한 줄로 간결하게 만들 때 사용한다.
# 사용법:
# 함수_이름 = lambda 매개변수1, 매개변수2, ...: 매개변수를_이용한_표현식
add = lambda a, b: a + b

result = add(3, 4)
print(result) # 7